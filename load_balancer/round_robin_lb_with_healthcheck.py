import socket
import threading
import requests
import time

class RoundRobinLoadBalancer:
    def __init__(self, backend_servers, health_check_url, health_check_period):
        self.backend_servers = backend_servers
        self.current_server_index = 0
        self.lb_socket = None
        self.health_check_url = health_check_url
        self.health_check_period = health_check_period
        self.active_servers = set()

    def handle_client(self, client_socket):
        with client_socket:
            data = client_socket.recv(1024)
            print(f"Received request from {client_socket.getpeername()}")
            print(data.decode('utf-8'))

            # Connect to the backend server based on round-robin
            backend_server_address = self.get_next_active_server()
            if backend_server_address is None:
                print("No active servers available.")
                return

            # Extract the path from the client's request
            path = data.decode('utf-8').split('\n')[0].split(' ')[1]

            # Forward the request to the backend server
            backend_url = f"http://{backend_server_address[0]}:{backend_server_address[1]}{path}"
            backend_response = requests.get(backend_url)

            # Print backend server's response
            print("\nResponse from server:", backend_response.text)

            # Forward the backend response to the client
            client_socket.sendall(backend_response.text.encode())

    def health_check_thread(self):
        while True:
            time.sleep(self.health_check_period)
            print("Performing health check...")

            for server_address in self.backend_servers:
                try:
                    response = requests.get(f"http://{server_address[0]}:{server_address[1]}{self.health_check_url}")
                    if response.status_code == 200:
                        print(f"Server {server_address} is healthy.")
                        self.active_servers.add(server_address)
                    else:
                        print(f"Server {server_address} is unhealthy (status code: {response.status_code}).")
                        self.active_servers.discard(server_address)
                except requests.RequestException as e:
                    print(f"Error during health check for server {server_address}: {e}")
                    self.active_servers.discard(server_address)

    def get_next_active_server(self):
        if not self.active_servers:
            return None

        # Round-robin selection from active servers
        server_address = list(self.active_servers)[self.current_server_index]
        self.current_server_index = (self.current_server_index + 1) % len(self.active_servers)
        return server_address

    def start_load_balancer(self, lb_address):
        # Start health check thread in the background
        health_check_thread = threading.Thread(target=self.health_check_thread, daemon=True)
        health_check_thread.start()

        # Start load balancer
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.lb_socket:
            self.lb_socket.bind(lb_address)
            self.lb_socket.listen()

            print("Load Balancer is listening on", lb_address)

            while True:
                client_socket, client_address = self.lb_socket.accept()
                # Handle each client connection in a separate thread
                threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    backend_servers = [('localhost', 5001), ('localhost', 5002), ('localhost', 5003)]  # Add a new server
    health_check_url = "/health"  # Change this to the actual health check endpoint on your servers
    health_check_period = 10  # Set the health check period in seconds

    load_balancer = RoundRobinLoadBalancer(backend_servers, health_check_url, health_check_period)
    load_balancer.start_load_balancer(('localhost', 8085))
