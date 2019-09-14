def vytvor_tabulku(velikost=11):
    seznam_radku = []
    for a in range(velikost):
        radek = []
        for b in range(velikost):
            radek.append(a * b)
        seznam_radku.append(radek)
    return seznam_radku

nasobilka = vytvor_tabulku()

print(nasobilka[2][3])  # dva krat tri
print(nasobilka[5][2])  # pet krat dva
print(nasobilka[8][7])  # osm krat sedum

# Vypsani cele tabulky
for radek in nasobilka:
    for cislo in radek:
        print(cislo, end=' ')
    print()

