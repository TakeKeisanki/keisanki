from threading import Thread

def my_function1():
  for i in range(10000):
    with lk1:
      print("123")
      print("456")
      print("789")

def my_function2():
  for i in range(10000):
    with lk2:
      print("abc")
      print("def")
      print("ghi")

def my_function3():
  for i in range(10000):
    print("ABC")
    print("DEF")
    print("GHI")

if __name__ == "__main__":
  lk1 = Rlock()
  lk2 = Rlock()
  t1 = Thread(target = my_function1)
  t2 = Thread(target = my_function2)
  t3 = Thread(target = my_function3)
  t1.start()
  t2.start()
  t3.start()
  t1.join()
  t2.join()
  t3.join()
