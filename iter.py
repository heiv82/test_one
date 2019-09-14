from itertools import count

for i in count(3):
    print(i, end=" ")
    if i >= 11:
        break

from itertools import accumulate, takewhile

print()
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)

print(power(2, 3))

