# Быстрая сортировка Хоара Python.
from random import randrange

def sort(a):
    if len(a) > 1:
        p = a[0]
        less = sort([x for x in a if x < p])
        greater = sort([x for x in a if x > p])
        return less + [x for x in a if x == p] + greater
    else:
        return a

list = [randrange(1, 20) for i in range(10)]
print(' '.join([str(s) for s in list]))
list_last = sort(list)
print(' '.join([str(i) for i in list_last]))
