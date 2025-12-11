import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Square {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube {i*i*i}")

if __name__ == "__main__":
    # Create processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = time.time()

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    elapsed = time.time() - start_time
    print(f"Total time: {elapsed:.2f} seconds")
