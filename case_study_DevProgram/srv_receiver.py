import socket
import os 

server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_socket.bind('/tmp/my_unix_socket')
server_socket.listen(1)

print("Server waiting for a connection...")
connection, client_address = server_socket.accept()

try:
  data = connection.recv(1024)
  print(f"Received: {data.decode()}")
finally:
  connection.close()
  server_socket.close()