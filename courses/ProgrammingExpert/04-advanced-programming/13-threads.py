import threading

def myThread(content):
    print(content)

thread1 = threading.Thread(target=myThread, args=("run 1",2)) # create a thread
thread2 = threading.Thread(target=myThread, args=("run 2",1)) # create a thread

thread1.start() # start the thread
thread2.start() # start the thread