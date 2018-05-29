from threading import Thread
from time import ctime, sleep, time

k = 0

def some_task():
    global k
    while True:
        k = k + 1


print('Start at', ctime(time()))
t = Thread(target=some_task, daemon=True)  # run the some_task function in another
t.start()
sleep(9)
print('Exit  at', ctime(time()))
print(k)
