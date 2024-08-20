import os 

fifo_path = '/tmp/my_fifo'

if not os.path.exists(fifo_path):
  os.mkfifo(fifo_path)

with open(fifo_path, 'w') as fifo:
  fifo.write("Hello from Aji")