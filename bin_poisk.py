from random import randrange



a = [randrange(1,50) for i in range(20)] # Create list throught randrange
print(' '.join([str(s) for s in a])) # print the created list

a.sort() # the list is sorted

print(' '.join([str(s) for s in a]))
x = 5
left = -1
right = len(a)
mid = 0
# Algoritmus praveho binarniho hledani prvku v seznamu


while left < right - 1:
    mid = (left + right) // 2
    if a[mid] > x:
        right = mid
    else:
        left = mid
if left >= 0 and a[left] == x:
    print(left)
else:
    print('Toto cislo tady neni!')