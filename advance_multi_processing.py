from concurrent.futures import ProcessPoolExecutor
import time

def square_time(number):
    time.sleep(1)
    return f"Square: {number * number}"

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Create a pool of processes
    with ProcessPoolExecutor(max_workers=2) as executor:
        results = executor.map(square_time, numbers)

    # Print results in order
    for result in results:
        print(result) 

