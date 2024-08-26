import socket 
import os 

client_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client_socket.connect('/tmp/my_unix_socket')

client_socket.sendall(b"Hello from Unix Socket")
client_socket.close()