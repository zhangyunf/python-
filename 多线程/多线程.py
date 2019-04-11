import threading
import time

def loop1(num):
    print('running on number %d' % num)
    time.sleep(3)

if __name__ == '__main__':

    t1 = threading.Thread(target=loop1, args=(1,))
    t2 = threading.Thread(target=loop1, args=(2,))
    t1.start()
    t2.start()
    print(t1.getName())
    print(t2.getName())
