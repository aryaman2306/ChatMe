#this is the code for server 

import socket
import threading

def handle_client(client_socket, address):
    print(f"Connection established with {address}")

    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            break
        print(f"Received message from {address}: {message}")

        # Broadcast the message to all connected clients
        for client in clients:
            if client != client_socket:
                client.sendall(message.encode("utf-8"))

    client_socket.close()
    print(f"Connection closed with {address}")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)

    print("Server started. Listening for incoming connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

clients = []

if __name__ == "__main__":
    start_server()

