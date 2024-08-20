import os

fifo_path = '/tmp/my_fifo'

with open(fifo_path, 'r') as fifo:
  message = fifo.read()
  print(f"Received message: {message}")