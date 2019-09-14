# Условие
# Напишите функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
# В этой задаче нельзя использовать циклы — используйте рекурсию.

def fib(n, first = 0, second = 1, number = 0, iterator = 2):
    if n != 0:
        number = first + second
        first, second = second, number
        if iterator < n:
            return fib(n, first, second, number, iterator + 1)
        else:
            return number
    else:
        return n

n = int(input())
print(fib(n))