#Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.



s = input()

one = s.find('h')
second = s.rfind('h')
print(s[:one] + s[second + 1:])