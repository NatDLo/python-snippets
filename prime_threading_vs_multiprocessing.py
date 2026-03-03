"""
Prime Number Benchmark – Threading vs Multiprocessing

This script computes the number of prime numbers below a given limit
and compares two concurrency models in Python:

1. ThreadPoolExecutor (threading)
2. multiprocessing.Pool (multiple processes)

The goal is to observe performance differences for a CPU-bound task.

Key concepts explored:
- CPU-bound workload
- Global Interpreter Lock (GIL)
- True parallelism with multiprocessing
- Function timing using decorators
- Profiling with cProfile

Expected behavior:
- Threading does NOT significantly improve performance due to the GIL.
- Multiprocessing achieves real parallelism across CPU cores.
"""

import os
import time
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

# Profiling tools
import cProfile
import pstats
from functools import wraps


# =========================
# Utility Decorators
# =========================

def timer_decorator(func):
    """
    Measures execution time of a function using high precision timing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        print(f"{func.__name__} --> {end - start:.6f} seconds")
        return result
    return wrapper


def profile_decorator(func):
    """
    Profiles a function using cProfile and prints cumulative time statistics.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()

        stats = pstats.Stats(profiler)
        stats.sort_stats(pstats.SortKey.CUMULATIVE)
        stats.print_stats()

        return result
    return wrapper


# =========================
# Prime Calculation (Threading Version)
# =========================

@profile_decorator
@timer_decorator
def count_primes_thread(n):
    """
    Counts prime numbers below n.
    Intended for ThreadPoolExecutor usage.
    """
    print(f"Thread PID {os.getpid()}")

    count = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count


# =========================
# Prime Calculation (Multiprocessing Version)
# =========================

@profile_decorator
@timer_decorator
def count_primes_process(n):
    """
    Counts prime numbers below n.
    Intended for multiprocessing.Pool usage.
    """
    print(f"Process ID {os.getpid()}, Parent PID {os.getppid()}")

    count = 0
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count


# =========================
# Main Execution
# =========================

if __name__ == "__main__":

    print(f"Main PID {os.getpid()}")

    ranges = [2_000_000, 2_000_000, 2_000_000, 2_000_000]

    # -------------------------
    # Threading version
    # -------------------------
    print("\n--- Threading Execution ---")
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        thread_results = list(executor.map(count_primes_thread, ranges))

    print(f"Threading total time: {time.time() - start_time:.2f} seconds")
    print(thread_results)

    # -------------------------
    # Multiprocessing version
    # -------------------------
    print("\n--- Multiprocessing Execution ---")
    start_time = time.time()

    with multiprocessing.Pool(processes=4) as pool:
        process_results = pool.map(count_primes_process, ranges)

    print(f"Multiprocessing total time: {time.time() - start_time:.2f} seconds")
    print(process_results)
