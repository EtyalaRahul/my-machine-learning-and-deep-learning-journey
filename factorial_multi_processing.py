'''
Real-world Example : Multi processing for cpu-bound tasks 
Scenario : Factorial Calculation 
Factorial Calculations, especially for larger numbers ,
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple
CPU cores, improving performance

'''

import multiprocessing 
import math  
import sys 
import time 

# REMOVE integer string conversion limit completely
sys.set_int_max_str_digits(0)

## function to compute factorial of a given number 
def compute_factorial(number):
    print(f"Computing factorial of {number}")
    res = math.factorial(number)
    return res 

if __name__=='__main__':
    numbers = [250]
    start_time = time.time()
    
    ## create a pool of worker process 
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)
    
    end_time = time.time()

    # PRINT FULL NUMBERS (this will be huge)
    print("Results :")
    for r in results:
        print(r)     # prints full factorial number

    print(f"Time taken : {end_time - start_time} seconds")
