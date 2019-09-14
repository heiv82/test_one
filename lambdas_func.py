print((lambda x: x**2 + 32 - 5 * x)(2))
print((lambda x: x**2)(3))
nums = [11, 22, 33, 44, 55,]

print(list(map(lambda x: x * 2, nums)))
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)