from time import sleep
def stream(nums):
    i = 0
    while True:
        i += 1
        yield i 
        sleep(1)
        
for i in stream(10):
    print(i)
    print('chera')

print('This is the second print')