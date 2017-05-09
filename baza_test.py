from osoba import *

os1 = osoba("Adam", "Kowalski", 23498754617)
os1.wypisz()
print(os1.pesel)

os2 = osoba("Jan", "Matejko", 7373947944946)
os3 = osoba("Janina", "Nowak", 4792379932659)

os2.wypisz()
os3.wypisz()
print(os1.spr_pesel())

#baza.append(os1)
#baza.append(os2)
#baza.append(os3)

#print(baza)

#for o in baza:
    #print(o.imie)