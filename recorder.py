import csv
import os
import time
import tracemalloc


def time_recorder(sort_algorithm, data):

    numbers = data.copy()                                #copy so the original data stays unosrted

    start = time.perf_counter()                          #record time using the difference between each timestamp
    sort_algorithm(numbers, 0, len(numbers) - 1)
    total_time = time.perf_counter() - start

    return total_time * 1000                             #seconds to milliseconds


def memory_recorder(sort_algorithm, data):

    numbers = data.copy()

    tracemalloc.start()
    sort_algorithm(numbers, 0, len(numbers) - 1)         #record peak memory consumption by the program
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return peak / 1024                                   #bytes to kilobytes


def save_results(algorithm_name, sort_algorithm, data, filename):

    ms = time_recorder(sort_algorithm, data)
    kb = memory_recorder(sort_algorithm, data)

    new_file = not os.path.exists("results.csv")         #check if results.csv already exists

    with open("results.csv", "a", newline="") as f:      #"a" adds a new row instead of overwriting

        writer = csv.writer(f)

        if new_file:
            writer.writerow(["algorithm", "file", "n", "time_ms", "peak_memory_kb"])

        writer.writerow([algorithm_name, filename, len(data), round(ms, 2), round(kb, 1)])

    print(f"{algorithm_name}  {filename}  n={len(data)}  {ms:.2f} ms  {kb:.1f} KB")