import sys

from file_parser import get_data
from quick_sort_random import quicksort_random_in_place
from quick_sort_deterministic import quick_sort_in_place
from recorder import save_results


sys.setrecursionlimit(100_000) 


if __name__ == "__main__":

    algorithm_choice = input("Choose which Quick Sort version to use: \n Quick Sort Random (r) \n ------------------ \n Quick Sort Deterministic (d) \n: ")

    

    if algorithm_choice == "d":
        name = "Quick Sort Deterministic"
        sort_algorithm = quick_sort_in_place

    elif algorithm_choice == "r":
        name = "Quick Sort Random"
        sort_algorithm = quicksort_random_in_place

    else:
        print("Wrong input, please restart the program and choose option \"r\" or \"d\" ")
        exit()


    filename = input("Select a file to get the data from for sorting: ")

    data = get_data(filename)
    print("Data before sorting: ", data)

    
    sorted_data = data.copy()

    sort_algorithm(sorted_data, 0, len(sorted_data) - 1)

    print("Data after sorting: ", sorted_data)

    save_results(name, sort_algorithm, data, filename)