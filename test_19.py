cislo = input('Zadejte cislo: ')

try:
	cislo1 = int(cislo)
except ValueError:
	print('To neni cislo ale stroka ')
	cislo1 = 0
print(cislo)