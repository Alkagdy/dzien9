from samochod3 import Samochod
from silnik import *

t8 = silnik(2000, 400, "Benzyna + prad")
print(t8.paliwo)

volvo = Samochod("Volvo", "XC60", t8)

print("{} {} ma sailnik {}".format(volvo.marka, volvo.model, volvo.silnik.V))

print("Silnik Volvo pracuje na: ", volvo.silnik.paliwo)



bmw = Samochod("BMW", "3", None)

silnik_bmw = silnik(3000, 180, "Diesiel")
bmw.silnik = silnik_bmw

print("Silnik bmw ma moc:", bmw.silnik.KM)

