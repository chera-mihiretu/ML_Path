import threading 
from time import sleep 
import concurrent.futures

lock = threading.Lock()

def task(fr):
    with lock:
        
        for i in range(2):
            print(f'Thread Task executed Thread {fr}')
        if fr == 2:
            sleep(2)



thread1 = threading.Thread(target=lambda : task(1))

thread2 = threading.Thread(target=lambda : task(2))

thread2.start()
thread1.start()

thread1.join()
thread2.join()