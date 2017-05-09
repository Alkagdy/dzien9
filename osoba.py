class osoba(object):

    '''definiuje informacje o osobach'''

    def __init__(self, imie, nazwisko, pesel):
        '''Inicjalizuje instancje klasy osoba'''
        self.imie = imie
        self.naziwsko = nazwisko
        self.wiek = None
        self.plec = None

        if len(str(pesel)) ==11:
            self.pesel = pesel
        else:
            print("Pesel musi mieć 11 znaków")
            self.pesel = None


    def wypisz(self):
        print(self.imie, self.naziwsko)

    def spr_pesel(self):
        if len(str(self.pesel)) == 11:
            return True
        return False



