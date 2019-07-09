my_list = [int(s) for s in input().split()]
for i in range(len(my_list)):
    for j in range(len(my_list)):
        if i != j and my_list[i] == my_list[j]:
            break
else:
    print(my_list[i], end=' ')
