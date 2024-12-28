
class Tevedlud:
    def __init__(self,yas,staj):
        self.yas = yas
        self.staj = staj

    def ekran(self):
        return  f"menim yasim {self.yas} menim is stajim {self.staj}"



class IlkSinif():
    def __init__(self,ad):
        self.ad = ad

    def salamla(self):
        print(f"Salam menim adin {self.ad}")


class AltSinif(IlkSinif,Tevedlud):

    def __init__(self,ad,mesaj,yas,staj):
        IlkSinif.__init__(self,ad)
        Tevedlud.__init__(self,yas,staj)
        self.mesaj = mesaj

    def cixiw(self):
        self.salamla()
        print(self.ekran())
        return self.mesaj







s = AltSinif('Shahin','Men cox yaxwiyam',48,15)


print(s.cixiw())
