import threading 
from time import sleep 
import concurrent.futures

lock = threading.Lock()

def task(fr):
       
        
        print(f'Thread Task executed Thread {fr}')
        sleep(2)



executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

for i in range(5):
    executor.submit(task, i)
executor.shutdown()
