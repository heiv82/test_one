#Дана строка. Замените в этой строке все цифры 1 на слово one.

n = input()
for i in list(n):
    if i == '1':
        print('one', end='')
    else:
        print(i, end='')

#print(input().replace('1', 'one')) the developers answer