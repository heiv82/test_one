def vyber_chybne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if jmeno[0].islower() or prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def vyber_spravne(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        if not jmeno[0].islower() and not prijmeni[0].islower():
            vysledek.append(zaznam)
    return vysledek

def oprava_chyb(seznam):
    vysledek = []
    for zaznam in seznam:
        jmeno_a_prijmeni = zaznam.split(' ')
        jmeno = jmeno_a_prijmeni[0]
        prijmeni = jmeno_a_prijmeni[1]
        vysledek.append(jmeno.capitalize() + ' ' + prijmeni.capitalize())
    return vysledek
zaznamy = ['pepa novak', 'Martin pedro', 'pavel Hong', 'Filip Kresavy']
print(vyber_chybne(zaznamy))
print(vyber_spravne(zaznamy))
print(oprava_chyb(zaznamy))