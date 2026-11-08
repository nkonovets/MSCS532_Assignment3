import random


def quicksort_random(data, left = 0, right = None): 

    if len(data) <= 1:                   # stop condition to return the already sorted array of data because it consists  
        return data                      # of only one number

    if right is None:
        right = len(data) - 1            # allows for the function to be called with only one parameter

    pivot = data.pop(random.randint(0, len(data) - 1))  #take a random number in the range from 0(index) to the length of the list passed

    rightpart = []                       # create two list to put the sorted numbers into
    leftpart = []
    even = [pivot]

    for i in data:                          # for loop that sorts the numbers and puts them into lists that are to the right or to the left of the pivot respectively

        if i > pivot:
            rightpart.append(i)
        elif i < pivot:
            leftpart.append(i)
        else:
            even.append(i)



    sorted_data = quicksort_random(leftpart) + even + quicksort_random(rightpart)
    return sorted_data                      # return the result of the both functions together, each time function is being called for every other sorted part of the list making the function recursive
    


def quicksort_random_in_place(numbers_list, left, right):
    numbers_list[left:right + 1] = quicksort_random(numbers_list[left:right + 1])



