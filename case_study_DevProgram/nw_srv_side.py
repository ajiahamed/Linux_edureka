import socket
server_socket = socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen(1)

print("Server waiting for a connection...")
connection, client_address = server_socket.accept()

try:
  data = connection.recv(1024)
  print(f"Received: {data.decode()}")
finally:
  connection.close()
  server_socket.close()