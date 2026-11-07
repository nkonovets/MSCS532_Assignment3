import sys

from file_parser import get_data
from merge_sort import merge_sort
from quick_sort import quick_sort_in_place
from recorder import save_results


sys.setrecursionlimit(100_000) 


if __name__ == "__main__":

    algorithm_choice = input("Choose an algorithm to use. \n Merge Sort(m) / Quick Sort(q): ")

    

    if algorithm_choice == "q":
        name = "Quick Sort"
        sort_algorithm = quick_sort_in_place

    elif algorithm_choice == "m":
        name = "Merge Sort"
        sort_algorithm = merge_sort

    else:
        print("Wrong input, please restart the program and choose option \"m\" or \"q\" ")
        exit()


    filename = input("Select a file to get the data from for sorting: ")

    data = get_data(filename)
    print("Data before sorting: ", data)

    
    sorted_data = data.copy()

    sort_algorithm(sorted_data, 0, len(sorted_data) - 1)

    print("Data after sorting: ", sorted_data)

    save_results(name, sort_algorithm, data, filename)