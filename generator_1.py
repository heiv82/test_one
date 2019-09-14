# Often used in conditional statements,
# all and any take a list as an argument,
# and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
# The function enumerate can be used to iterate through the values and indices of a list simultaneously.


nums = [55, 34, 56, 78, 21, 35]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At list one is even")

nums.sort()

for v in enumerate(nums):
    print(v)
