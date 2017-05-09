class Samochod(object):
    def __init__(self,marka,model,kolor):
        self.marka = marka
        self.model = model
        self.kolor = kolor
        self.czy_jedzie = False
        self.silnik = None


        #argumenty z nawiasu sa po prawej stronie. Po lewej mozna by inaczej nazwac

    def jedz(self):
        print(self.marka, ":Jade")
        self.czy_jedzie = True

    def zatrzymaj(self):
        self.czy_jedzie = False

