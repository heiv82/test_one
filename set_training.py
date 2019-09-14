nums = set([1, 2, 3, 4, 5, 6, 7])
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
nums.pop()
print(nums)
first = {1, 2, 3, 4, 5}
second = {4, 5, 9, 10}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)