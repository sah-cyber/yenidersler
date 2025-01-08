class Bilet:
    def __init__(self, neqliyyat, qiymet, nov):
        self.neqliyyat = neqliyyat
        self.qiymet = qiymet
        self.nov = nov


class Hava(Bilet):
    def yol(self):
        print(f"Neqliyyat: {self.neqliyyat}, Qiymet: {self.qiymet}, Nov: {self.nov} Hava yolu ile")


class Demiryol(Bilet):
    def yol(self):
        print(f"Neqliyyat: {self.neqliyyat}, Qiymet: {self.qiymet}, Nov: {self.nov} Demir yolu ile")


class Suyol(Bilet):
    def yol(self):
        print(f"Neqliyyat: {self.neqliyyat}, Qiymet: {self.qiymet}, Nov: {self.nov} Su yolu ile")


neqliyatvasite = [
    Demiryol('Qatar', 120, 'A class'),
    Suyol('Gemi', 80, 'B class'),
    Hava('Teyyare', 500, 'C class')
]

for yol in neqliyatvasite:
    yol.yol()

print('*'*30)
class Oyuncu:
    def __init__(self, name,position,enerji):
        self.name = name
        self.position = position
        self.enerji = enerji


class Solider(Oyuncu):
    def hereket_et(self):
        print('Esker Hereket etdi')
        print(f"Esger adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")

class Employee(Oyuncu):

    def hereket_et(self):
        print('Isci Hereket etdi')
        print(f"Isci adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")


class Driving(Oyuncu):

    def hereket_et(self):
        print('Surucu Hereket etdi')
        print(f"Surucu adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")


def basla():
    shahin = Solider('Shahin','komandir',100)
    musa = Driving('Musa','surucu',80)
    elmir = Employee('Elmir','elektrik',60)


    oyuncular = [shahin,musa,elmir]
    for oyuncular in oyuncular:
        oyuncular.hereket_et()


basla()


from abc import ABC, abstractmethod
class Oyuncu(ABC):
    def __init__(self, name,position,enerji):
        self.name = name
        self.position = position
        self.enerji = enerji

    @abstractmethod
    def hereket_et(self):
        pass


class Solider(Oyuncu):
    def hereket_et(self):
        print('Esker Hereket etdi')
        print(f"Esger adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")




class Employee(Oyuncu):

    def hereket_et(self):
        print('Isci Hereket etdi')
        print(f"Isci adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")



class Driving(Oyuncu):

    def hereket_et(self):
        print('Surucu Hereket etdi')
        print(f"Surucu adi: {self.name},Vesifesi {self.position}, enerji {self.enerji}")



shahin = Solider('Shahin','komandir',100)
musa = Driving('Musa','surucu',80)
elmir = Employee('Elmir','elektrik',60)




shahin.hereket_et()
musa.hereket_et()
elmir.hereket_et()



class Insan:
    def __init__(self, name, dogum_ili):
        self.name = name
        self.dogum_ili = dogum_ili


    @property
    def age(self):
        cari_il = 2025
        return cari_il - self.dogum_ili

    @age.setter
    def age(self,yeni_yas):
        print('yas deyeri deyisdirile bilmez')


    @age.deleter
    def age(self):
        print('yas deyeri silinib')
        del self.dogum_ili



insan = Insan('shahin', 1983)


class Data:
    def __init__(self):
        self.data = 10


    @property
    def veri(self):
        return self.data


    @veri.setter

    def veri(self, yeni_deyer):
        self.data = yeni_deyer
        return yeni_deyer


    @veri.deleter
    def veri(self):
        print('deyer silindi')
        del self.data


s = Data()

s.veri = 15
print(s.veri)
print(s.data)
del s.veri

