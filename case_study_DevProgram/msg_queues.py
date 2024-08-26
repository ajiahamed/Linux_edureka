from multiprocessing import Process, Queue

def producer(queue):
  queue.put("Hello from producer")

def consumer(queue):
  message = queue.get()
  print(f"Consumer received message: {message}")

if __name__ == "__main__":
  queue = Queue()
  p1 = Process(target=producer, args=(queue,))
  p2 = Process(target=consumer, args=(queue,))

  p1.start()
  p2.start()

  p1.join()
  p2.join()