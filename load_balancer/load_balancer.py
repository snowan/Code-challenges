import socket
import threading

def handle_client(client_socket):
    with client_socket:
        data = client_socket.recv(1024)
        print(f"Received request from {client_socket.getpeername()}")
        print(data.decode('utf-8'))

        # Connect to the backend server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
            backend_socket.connect(('localhost', 8081))
            backend_socket.sendall(data)

            # Receive response from backend
            backend_response = backend_socket.recv(1024)
            print("\nResponse from server:", backend_response.decode('utf-8'))

            # Forward the backend response to the client
            client_socket.sendall(backend_response)

def load_balancer():
    lb_address = ('localhost', 8080)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as lb_socket:
        lb_socket.bind(lb_address)
        lb_socket.listen()

        print("Load Balancer is listening on", lb_address)

        while True:
            client_socket, client_address = lb_socket.accept()
            # Handle each client connection in a separate thread
            threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()

if __name__ == "__main__":
    load_balancer()
