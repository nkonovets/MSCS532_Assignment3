import random

numbers = [5, 1, 8, 4, 9, 6, 4, 2, 3]

def quicksort_random(data, left = 0, right = None):

    if len(data) <= 1:
        return data

    if right is None:
        right = len(data) - 1

    pivot = data.pop(random.randint(0, len(data) - 1))

    rightpart = []
    leftpart = []

    for i in data:

        if i >= pivot:
            rightpart.append(i)

        elif i < pivot:
            leftpart.append(i)

    


    return quicksort_random(leftpart) + [pivot] + quicksort_random(rightpart)
    

print(quicksort_random(numbers))
    



