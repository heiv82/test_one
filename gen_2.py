def nums(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(nums(11)))