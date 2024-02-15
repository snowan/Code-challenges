import socket
import threading
import requests

class RoundRobinLoadBalancer:
    def __init__(self, backend_servers):
        self.backend_servers = backend_servers
        self.current_server_index = 0
        self.lb_socket = None

    def handle_client(self, client_socket):
        with client_socket:
            data = client_socket.recv(1024)
            print(f"Received request from {client_socket.getpeername()}")
            print(data.decode('utf-8'))

            # Connect to the backend server based on round-robin
            backend_server_address = self.backend_servers[self.current_server_index]
            self.current_server_index = (self.current_server_index + 1) % len(self.backend_servers)

            # Extract the path from the client's request
            path = data.decode('utf-8').split('\n')[0].split(' ')[1]

            # Forward the request to the backend server
            backend_url = f"http://{backend_server_address[0]}:{backend_server_address[1]}{path}"
            backend_response = requests.get(backend_url)
            print(f"backend url: {backend_url}, backend response {backend_response}")

            # Print backend server's response
            print("\nResponse from server:", backend_response.text)

            # Forward the backend response to the client
            client_socket.sendall(backend_response.text.encode())

    def start_load_balancer(self, lb_address):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.lb_socket:
            self.lb_socket.bind(lb_address)
            self.lb_socket.listen()

            print("Load Balancer is listening on", lb_address)

            while True:
                client_socket, client_address = self.lb_socket.accept()
                # Handle each client connection in a separate thread
                threading.Thread(target=self.handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    backend_servers = [('localhost', 5001), ('localhost', 5002)]  # Flask default ports
    load_balancer = RoundRobinLoadBalancer(backend_servers)
    load_balancer.start_load_balancer(('localhost', 8082))
