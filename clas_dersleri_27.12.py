


class Personal:
    def __init__(self):
        self.personal_yarat()


    def personal_yarat(self):
        for i in range(2):
            self.personal_name = input(f'{i+1} Personal name ')
            self.personal_mmaw = int(input(f'{i+1} Personal maaw '))

            maaw_cem = self.personal_mmaw + (self.personal_mmaw *0.20)
            print(f"personal {self.personal_name}, 20% artimli maawi {maaw_cem}")


Personal()


class Pul_hesabla:
    def __init__(self,faiz):
        self.faiz=faiz
        self.hesabla()

    def hesabla(self,faiz_derecesi = 11/100):

        self.cem = (self.faiz * faiz_derecesi)*3
        self.cem1 = (self.faiz * faiz_derecesi)*2
        self.cem2 = (self.faiz * faiz_derecesi)

        print(f"Goturduyunuz {self.faiz} AZN mebleginin 3 illik 11 faiz derecesi {self.cem} AZN")
        print(f"Goturduyunuz {self.faiz} AZN mebleginin 2 illik 11 faiz derecesi {self.cem1} AZN")
        print(f"Goturduyunuz {self.faiz} AZN mebleginin 1 illik 11 faiz derecesi {self.cem2} AZN")


emp1 = Pul_hesabla(faiz=int(input('Meblegi qeyd edin: ')))



class Kredit():
    def _init_(self, esas, illik_faiz, iller):
        self.esas=esas
        self.illik_faiz = illik_faiz
        self.iller = iller

    def total_odenis(self):
        umumi_mebleg = self.esas*(1+(self.illik_faiz/100)*self.iller)
        return umumi_mebleg
kredit = Kredit(10000, 11, 3)
total = kredit.total_odenis()
print(f"Umumi odenis {kredit.iller} ilden sonra: {total:.2f} AZN teskil edecek")


class Book:
    def __init__(self, title, author,year):
        self.title = title
        self.author = author
        self.year = year


    def info(self):
        print(f"Adi: {self.title} Yazar:{self.author} Cap ili:{self.year}")

book = Book('Nagillar','Xalq edebiyyati','1999')
book.info()
book1 = Book('Sehidler','B.Vahabzade','1990')
book1.info()



class BankAcound:
    def __init__(self,acound_holder,balance=0):
        self.acound_holder=acound_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance

    def withdraw(self,amount):
        self.balance=self.balance-amount
        return self.balance

    def get_balance(self):
        return self.balance

bank1 = BankAcound(1,100)
print(bank1.balance)

print(bank1.deposit(5))
print(bank1.withdraw(2))
print(bank1.get_balance())


class Sdudent:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Telebenin adi: {self.name} Yasi: {self.age}'

class Curs:
    def __init__(self,instruktor,courses_name):
        self.instruktor = instruktor
        self.courses_name = courses_name

    def shof_course(self):
        print(f"Instruktor: {self.instruktor},Kurslar: {self.courses_name}")

telebe1=Sdudent('Anar',18)
print(telebe1)
kurs_1 = Curs('Vadim','JavaScript,Python')
kurs_1.shof_course()



import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi *self.radius **2

    def circumference(self):
        return 2 * math.pi *self.radius


cirkle1= Circle(10)


print(f"Dairenin sahesi: {cirkle1.area():.3f}")

print(f"Dairenin Cevresi {cirkle1.circumference():.3f}")




