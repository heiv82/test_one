number = 23
run = True

while run:
    guess = int(input('Please input a whole number: '))

    if guess == number:
        print('Gratulations , you are won!')
        run = False
    elif guess < number:
        print('This number is greater')
    else:
        print('This number is smaller')
else:
    print('The loop is finish')
print('The end')