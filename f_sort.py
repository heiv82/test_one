# Быстрая сортировка Хоара Python.
from random import randrange

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of
        return array
list = [randrange(1, 20) for i in range(10)]
print(' '.join([str(s) for s in list]))
list_last = sort(list)
print(' '.join([str(i) for i in list_last]))
