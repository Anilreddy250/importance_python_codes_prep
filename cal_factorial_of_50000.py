import time
import multiprocessing
import math
import sys

# Factorials of 50,000 are massive. 
# We need to increase the limit for integer string conversion to handle it.
sys.set_int_max_str_digits(0) 

def calculate_factorial(n):
    """The heavy lifting."""
    return math.factorial(n)

def run_sequential(n, iterations):
    start = time.perf_counter()
    for _ in range(iterations):
        calculate_factorial(n)
    return time.perf_counter() - start

def run_multiprocessing(n, iterations):
    start = time.perf_counter()
    # Create a pool of 4 processes
    with multiprocessing.Pool(processes=iterations) as pool:
        pool.map(calculate_factorial, [n] * iterations)
    return time.perf_counter() - start

if __name__ == "__main__":
    NUMBER = 50000
    REPS = 4

    print(f"--- Task: Calculate {NUMBER}! {REPS} times ---\n")

    # 1. Standard For Loop
    print("Running sequentially...")
    seq_time = run_sequential(NUMBER, REPS)
    print(f"Total Sequential Time: {seq_time:.4f}s")

    # 2. Multiprocessing
    print("\nRunning with multiprocessing...")
    multi_time = run_multiprocessing(NUMBER, REPS)
    print(f"Total Multiprocessing Time: {multi_time:.4f}s")

    # 3. The Verdict
    speedup = seq_time / multi_time
    print(f"\nConclusion: Multiprocessing is {speedup:.2f}x faster.")
# def factorial(n):
#     if n<=0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(50000))
