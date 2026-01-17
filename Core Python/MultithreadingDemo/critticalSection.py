from threading import Thread, Lock
import time

def withdraw(amt):
    lock.acquire()
    with open('MultithreadingDemo/account.txt', 'r') as fp:
        content = fp.read()
        bal = int(content)
        bal -= amt
    
    with open('MultithreadingDemo/account.txt', 'w') as fp:
        fp.write(str(bal))
    lock.release()

def deposite(amt):
    lock.acquire()
    with open('MultithreadingDemo/account.txt', 'r') as fp:
        content = fp.read()
        bal = int(content)
        bal += amt
    
    with open('MultithreadingDemo/account.txt', 'w') as fp:
        fp.write(str(bal))
    lock.release()

if(__name__ == '__main__'):
    lock = Lock()
    t2 = Thread(name='Thread2', target=deposite, args=(5000, ))
    t1 = Thread(name='Thread1', target=withdraw, args=(3000, ))
    t1.start()
    t2.start()