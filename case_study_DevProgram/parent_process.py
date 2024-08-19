import os 

def parent():
  r, w = os.pipe()
  pid = os.fork()

  if pid:
    #Parent process 
    os.close(r)
    with os.fdopen(w, 'w') as pipe_out:
      pipe_out.write("Hello from parent")
  else:
    #Child process
    os.close(w)
    with os.fdopen(r, 'r') as pipe_in:
      message = pipe_in.read()
      print(f"Child received message: {message}")

if __name__ == "__main__":
  parent()
