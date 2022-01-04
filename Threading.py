import threading


class GuyMessenger(threading.Thread):
    def run(self):
        # _ mean don't care about the variable in the loop
        for _ in range(10):
            print(threading.current_thread().getName())


x = GuyMessenger(name='Send out messages')
y = GuyMessenger(name='Receive messages')

x.start()
y.start()
