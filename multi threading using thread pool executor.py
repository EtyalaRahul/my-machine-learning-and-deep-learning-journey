## Multithreading with thread pool executor


from concurrent.futures import ThreadPoolExecutor 
import time 

def print_numbers(number) :
    time.sleep(1)
    return f"Number : {number}"

numbers=[1,2,3,4,5,3,3,4,5,3,3,2,4,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,3,3]


with ThreadPoolExecutor(max_workers=300) as executor :
    results=executor.map(print_numbers,numbers) 
    
for result in results :
    print(result)