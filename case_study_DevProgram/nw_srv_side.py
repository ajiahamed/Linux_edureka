import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.29.129', 65432))
server_socket.listen(1)

print("Server waiting for a connection from remote client...")
connection, client_address = server_socket.accept()

try:
  data = connection.recv(1024)
  print(f"Received: {data.decode()}")

finally:
  connection.close()
  server_socket.close()