from samochod2 import *

auto1 = Samochod("Toyota", "Jaris", "Niebieska")
print(auto1.marka)
print(auto1.model)
print(auto1.kolor)

print(auto1.silnik)
auto1.silnik = "1.0 90 km"
print(auto1.silnik)

auto1.il_drzwi = 3
print(auto1.il_drzwi)

auto1.jedz()
print(auto1.czy_jedzie)

auto2 = Samochod("Volvo", "XC60 nowe", "Dark Grey")
print(auto2.marka)
print(auto2.model)
print(auto2.kolor)
auto2.jedz()

auto1.zatrzymaj()
print(auto1.czy_jedzie)
