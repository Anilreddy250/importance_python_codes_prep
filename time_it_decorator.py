import time
from functools import wraps

def time_it(func):
    """Decorator that reports the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record the start time using high-precision perf_counter
        start_time = time.perf_counter()
        
        # Execute the actual function
        result = func(*args, **kwargs)
        
        # Record the end time
        end_time = time.perf_counter()
        
        # Calculate duration
        duration = end_time - start_time
        
        print(f"DEBUG: Function '{func.__name__}' executed in {duration:.6f} seconds")
        return result
        
    return wrapper

# --- Example Usage for a Math Library ---

@time_it
def compute_factorial(n):
    """Computes the factorial of a number."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

@time_it
def simulate_heavy_calc():
    """Simulates a complex mathematical process."""
    time.sleep(0.5)  # Artificial delay
    return sum(range(1000000))

# Testing the suite
if __name__ == "__main__":
    compute_factorial(5000)
    simulate_heavy_calc()