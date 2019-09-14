osoby = 'mama', 'teta', 'tato'
vlastnosti = 'hodna', 'mila', 'laskavy'
for osoba, vlastnost in zip(osoby, vlastnosti):
    print('{} je {}'.format(osoba, vlastnost))