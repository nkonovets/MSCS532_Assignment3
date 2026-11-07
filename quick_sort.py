def quick_sort(sequence):
    lenght = len(sequence)

    if lenght <= 1:
        return sequence
    else:
        pivot = sequence.pop()  #I take the last item as the pivot

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)


    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)



def quick_sort_in_place(numbers_list, left, right):      #added a function for recorder to work with quicksort

    sorted_part = quick_sort(numbers_list[left:right + 1])
    numbers_list[left:right + 1] = sorted_part          #put the sorted numbers back into the original list