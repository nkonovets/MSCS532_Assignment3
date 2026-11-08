# MSCS532 Assignment 3: Algorithm Efficiency and Scalability

Randomized Quicksort compared with deterministic Quicksort, and a hash table with chaining.
The full report is in [report/REPORT.md](report/REPORT.md).

## Files

- `quick_sort_random.py` – Quicksort with a random pivot and a separate list for repeated values
- `quick_sort_deterministic.py` – Quicksort with the first element as the pivot
- `hash_table.py` – hash table with chaining, universal hashing and resizing
- `main.py` – runs a sort on a data file and saves time and memory to `results.csv`
- `recorder.py`, `file_parser.py` – timing, memory and file reading helpers
- `data/` – random, sorted, reverse-sorted and repeated-value inputs (1,000 / 10,000 / 50,000 numbers)

`quick_sort_deterministic.py`, `recorder.py`, `file_parser.py` and most of the `data/` files are adapted from my Assignment 2.

## How to run

Requires Python 3.

Quicksort (choose `r` or `d`, then enter a file such as `data/sorted_large.txt`):

```bash
python3 main.py
```

To run all 24 tests at once:

```bash
for alg in r d; do
  for kind in random sorted reverse repeated; do
    for size in small mid large; do
      printf "$alg\ndata/${kind}_${size}.txt\n" | python3 main.py > /dev/null
    done
  done
done
```

Hash table demo:

```bash
python3 hash_table.py
```

## Summary of findings

- On random input both Quicksorts are fast, about 37–45 ms at 50,000 numbers.
- On sorted and reverse-sorted input the deterministic version hits its O(n²) worst case and takes about 33–35 seconds at 50,000 numbers, while the random version stays around 37 ms.
- On repeated values the random version is the fastest (5 ms at 50,000 numbers) because equal numbers are placed in one step.
- The hash table keeps insert, search and delete at O(1) on average by doubling its size when the load factor goes above 0.75.
