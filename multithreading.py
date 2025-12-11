## multhi threading
## when to use multithreading
## i/o bound tasks : Tasks that spend more time waiting for i/o operations (e.g,. file operations,network requests).
### concurrent exectuion : When you want to improve the throughput of your applcation by performing multiple opearations concurrently 

import threading 
import time 


def print_numbers() :
    for  i in range(5) :
        time.sleep(2)
        print(f"Number : {i}")
        
        
def print_letters() :
    for letter in "abcdef" :
        time.sleep(2)
        print(f"Letter : {letter}")
        
        
##create 2 threads 
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letters)
t=time.time()      

## start threads 
t1.start()
t2.start() 

## wait for the entire threads to complete
t1.join()
t2.join()

fineshed_time=time.time()-t 
print(fineshed_time) 

