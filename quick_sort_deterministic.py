def quick_sort(data):
    lenght = len(data)

    if lenght <= 1:
        return data
    else:
        pivot = data.pop(0)  #This time I take the first number in the list as a pivot

    rightpart = []
    leftpart = []              # create two list to put the sorted numbers into

    for item in data:
        if item > pivot:
            rightpart.append(item)

        else:
            leftpart.append(item)


    return quick_sort(leftpart) + [pivot] + quick_sort(rightpart)



def quick_sort_in_place(numbers_list, left, right):      #added a function for recorder to work with quicksort

    sorted_part = quick_sort(numbers_list[left:right + 1])
    numbers_list[left:right + 1] = sorted_part          #put the sorted numbers back into the original list