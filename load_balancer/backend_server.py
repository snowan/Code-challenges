import socket

def backend_server():
    server_address = ('localhost', 8081)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server_address)
        server_socket.listen()

        print("Backend Server is listening on", server_address)

        while True:
            connection, client_address = server_socket.accept()
            with connection:
                print(f"Received request from {client_address}")
                data = connection.recv(1024)
                print(data.decode('utf-8'))
                print("\nReplied with a hello message")
                connection.sendall(b"HTTP/1.1 200 OK\n\nHello From Backend Server")

if __name__ == "__main__":
    backend_server()
