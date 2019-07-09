while True:
    s = input('Please to take input a number: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('The number is too small.')
        continue
    print('The string is fit!')
