





# Feladat 1.
# add meg az adatok sorainak a számát (az első sor nélkül)
from FilmClass import Film


def fajlbeolvasas():
	file = open("film.txt","r",encoding="UTF-8")
	file.readline()
	sorokLista = file.readlines()
	file.close()

	filmLista = []
	for i in range(len(sorokLista)):
		aktElem = sorokLista[i]
		sorLista = aktElem.strip().split(";")
		cim = str(sorLista[0])
		rendezo = str(sorLista[1])
		foszereplo = str(sorLista[2])
		ev = int(sorLista[3])
		perc = int(sorLista[4])

		film = Film(cim,rendezo,foszereplo,ev,perc)
		filmLista.append(film)

	return filmLista

lista = fajlbeolvasas()






# Feladat 2.
def SorokSzama():
	db = len(lista)
	return db






# Feladat 3.
# Melyik a legrövidebb film címe?
def Legrovidebb():
	legrov = 999
	for i in range(len(lista)):
		if lista[i].perc < legrov:
			legrov = lista[i].perc
			cim = lista[i].cim
	return cim






# Feladat 4.
#Hány darab legalább 110 perces film van?
def SzazTiz():
	szamlalo = 0
	for i in range(len(lista)):
		if lista[i].perc >= 110:
			szamlalo += 1
	return szamlalo






# Feladat 5.
# Kérd be egy színész nevét, és ajánlj egy pár filmet a készletből, 
# ha tudsz (film címét íratjuk ki, ha van ilyen)! Ha nincs ilyen nevű színész, akkor azt is tudasd!
def Ajanlas():
	szinesz = str(input("Kérek egy színész nevet: "))
	




































# Feladat: 
#Sorsolj ki egy pozitív egész számot, ami legfeljebb 1 milliárd lehet.
#Add össze a szám számjegyeit, majd a kapott szám számjegyeit ismét add össze.
#Addig ismételd, amíg egyetlen számjegy nem marad, majd írd ki a végeredményt.
#Az ellenőrzés megkönnyítése érdekében a köztes eredményeket is írd ki!
#Példa: 13637648 38 11 2


import random

def OsszeadMindenSzamjegy():
	szam, osszeg = 0, 0
	szam = random.randint(0,1000000000)
	print(f"Kapott számunk:{szam}")
	szam_str = str(szam)

	while not osszeg > 0 and osszeg < 10:
		for i in range(len(szam_str)):
			osszeg += int(szam_str[i])
	print(f"szam: {osszeg}")
	# meg nincs kesz

#OsszeadMindenSzamjegy()
