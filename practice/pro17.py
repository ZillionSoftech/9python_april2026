import threading


def display():
    for i in range(5):
        print("Thread Running")


thread1 = threading.Thread(target=display)
thread1.start()
thread1.join()