import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.29.129', 65432))

client_socket.sendall(b"Hello from network socket")
client_socket.close()