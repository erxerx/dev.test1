from threading import Thread
from time import ctime, sleep, time

k = 0


def some_task():
    global k
    while True:
        k = k + 1


t = Thread(target=some_task)  # run the some_task function in another
# thread
t.daemon = True  # Python will exit when the main thread
# exits, even if this thread is still
# running
print('Start at', ctime(time()))
t.start()
sleep(9)
print('Exit  at', ctime(time()))
print(k)
