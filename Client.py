import socket
import threading
import tkinter as tk

def receive_data(client_socket, chat_text):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            chat_text.config(state=tk.NORMAL)
            chat_text.insert(tk.END, "Other: " + data.decode() + "\n")
            chat_text.config(state=tk.DISABLED)
        except Exception as e:
            print("Error receiving data:", e)
            break

    client_socket.close()

def send_message(client_socket, message, entry_text):
    message = entry_text.get()
    entry_text.delete(0, tk.END)

    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "You: " + message + "\n")
    chat_text.config(state=tk.DISABLED)

    client_socket.sendall(message.encode())

def start_client():
    host = '127.0.0.1'
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    client_window = tk.Tk()
    client_window.title("Client")

    chat_text = tk.Text(client_window, wrap=tk.WORD, state=tk.DISABLED)
    chat_text.pack(fill=tk.BOTH, expand=True)

    entry_text = tk.Entry(client_window, width=50)
    entry_text.pack(pady=10)

    send_button = tk.Button(client_window, text="Send", command=lambda: send_message(client_socket, entry_text))
    send_button.pack()

    receive_thread = threading.Thread(target=receive_data, args=(client_socket, chat_text))
    receive_thread.start()

    client_window.mainloop()

if __name__ == '__main__':
    start_client()
