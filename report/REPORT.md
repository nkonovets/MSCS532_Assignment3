# Assignment 3: Understanding Algorithm Efficiency and Scalability

## Report

## Part 1: Randomized quicksort

Quick_sort_random.py selects a random number from the list as the pivot by removing it from the initial data list with pop() and storing it in the pivot variable. After this, it compares each number in the list with the pivot and places it in the list of values greater than the pivot and the list of values less than the pivot. The even[] list contains values equal to the pivot. I decided to implement this version of the quicksort algorithm because I used the same list-based version during the last assignment. After the initial sorting, the left and right parts of the list are passed to the same function recursively in the return statement, so in the end the function combines all the lists, yielding the sorted list.

### Average-case analysis

To analyze the average case, I count the total number of comparisons quick_sort_random.py makes, assuming all numbers in the list are distinct. Two numbers are only compared when one of them is the pivot, and after that they are never compared again, because the pivot is not passed to the next recursive calls. To count this, I use an indicator random variable for each pair of numbers, which is 1 if the pair is compared and 0 otherwise. The expected number of comparisons is then the sum of the probabilities that each pair is compared.

If we take two numbers from the sorted order, they stay in the same list until one of the numbers between them (including them) is chosen as the pivot. If the first pivot chosen from that range is one of the two numbers, then the two numbers are compared. If it is any number in between, it goes into different lists and is never compared. Because the pivot is chosen randomly, each number in that range has the same chance of being picked first, so the probability that the two numbers are compared is 2 divided by the range's size. When I add these probabilities for all pairs, each number contributes about 2 ln n comparisons, and with n numbers, the total is O(n log n). Because the pivot is random, this is the expected time for any input, even if the list is already sorted.

### Results

As I described in Assignment 2 last week, the quicksort algorithm performs well on a random data set. And this time, both of the quicksort algorithms showed really good time and memory results. At 50,000 numbers, the deterministic version took 36.57 ms, and the random version took 44.81 ms, indicating that, in my case, the deterministic version is still slightly faster than the quicksort with the random pivot.

The real difference comes in place when comparing both types of quicksort on the sorted and reverse-sorted sets of data, and the difference is huge. The deterministic version always takes the first number as the pivot, which, in a sorted or reverse-sorted list, is always the smallest or largest number, so every split leaves almost all the numbers on one side. That is where deterministic quicksort hits its worst case. Sorting the set of 50,000 numbers took 34.7 seconds, while the random quicksort took a blazing 36.72 ms, which truly shows the difference between two versions of the same algorithm.

In contrast, on the set with repeated values, the random version was the fastest of all, and took only 5.03 ms to sort the list with 50,000 numbers. This speed comes from the fact that the even[] list places all equal numbers in one step.

| Input          |      n | Deterministic Memory (KB) | Deterministic Time (ms) | Random Memory (KB) | Random Time (ms) |
| -------------- | -----: | ------------------------: | ----------------------: | -----------------: | ---------------: |
| Random         |  1,000 |                      40.9 |                    0.56 |               39.8 |             0.62 |
|                | 10,000 |                     509.4 |                    6.19 |              417.1 |             7.69 |
|                | 50,000 |                   2,531.4 |                   36.57 |            2,194.9 |            44.81 |
| Sorted         |  1,000 |                   4,326.7 |                   12.40 |               39.1 |             0.57 |
|                | 10,000 |                 407,475.9 |                1,074.56 |              405.6 |             7.27 |
|                | 50,000 |               9,177,641.1 |               34,726.40 |            2,103.1 |            36.72 |
| Reverse-sorted |  1,000 |                   4,292.6 |                   12.11 |               36.6 |             0.57 |
|                | 10,000 |                 416,621.2 |                1,166.49 |              415.3 |             7.15 |
|                | 50,000 |              10,362,581.9 |               32,986.66 |            2,200.2 |            37.34 |
| Repeated (0–9) |  1,000 |                     104.6 |                    1.57 |               39.5 |             0.13 |
|                | 10,000 |                   5,082.2 |                  108.42 |              356.7 |             1.15 |
|                | 50,000 |                 111,472.2 |                2,481.97 |            1,986.4 |             5.03 |

## Part 2: Hash Tables

### Implementation

In my hash_table.py, each slot contains a list, so if multiple keys are assigned to the same slot, they would not overwrite each other. My hash table can do simple operations such as insert(), search(), and delete() on entities in the table. For testing purposes, I have added a test list of people's names that need to be stored in the table, and tested these three operations: finding, deleting, and inserting values in the table. To decide where each key goes, I used a universal hash function with two randomly chosen numbers. This helps reduce the chance of repeated collision patterns.

### Analysis

One important factor affecting the performance of my hash table is the load factor (α). I calculated it by dividing the number of stored keys by the total number of slots. Since my implementation uses chaining, a higher load factor means that more keys are stored in each list on average. This makes searching for a specific key more time-consuming, and the expected time complexity of the operations is O(1 + α).

To prevent the lists from becoming too long, I made the table automatically double its size whenever the load factor exceeds 0.75. Although resizing requires additional time because the existing keys need to be redistributed, it does not happen during every insertion. By keeping the load factor below this limit, the table can maintain an average time complexity of O(1) for insertion, searching, and deletion.
