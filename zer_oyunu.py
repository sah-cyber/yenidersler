

import random
import time


class Zerler:

    def __init__(self):
        print('Oyuna xow Gelmisiniz')

        self.list_adlar = ['Aydan', 'Nubar', 'Lale', 'Orxan', 'Cavid']
        print(
            '''Zer atisi oyununa xosh gelmisiniz! Oyununa baslamaq ucun 'enter' cixmaq isteyirsinizse 'Q' duymesini basin''')

        self.control()


    def control(self):
        self.start = input('Seciminiz: ')
        if self.start.lower() == 'q':
            print('Cox Tesuf oyunu terk etdiniz...')
        else:
            self.menu()


    def menu(self):
        self.ad_yaz = random.choice(self.list_adlar)
        print("\nSalam size xidmet edir '{}!'\n"
              "Zehmet olmasa udusunuzu edin ve hansi zer gelisini deyin!".format(self.ad_yaz))
        self.ad_yoxla()


    def ad_yoxla(self):
        self.adiniz = input('Zehmet olmasa adinizi qeyd edin: ')
        if self.adiniz.isalpha() and len(self.adiniz) > 2:
            self.udusu_yoxla()
        else:
            print('secimi duzgun edin reqem ve 3 herfden qisa ad olmaz')
            self.ad_yoxla()


    def udusu_yoxla(self):
        self.udus = input("Udusunuzu elave edin: ")
        if self.udus.isdigit() and int(self.udus) > 0:
            print(f"Tewekur edirem '{self.adiniz.capitalize()}' Siz {self.udus} AZN udus meblegi qoydunuz!")
            print('*' * 50)
            self.udus = int(self.udus)
            self.birinci = self.udus * 1.50
            self.ikinci = self.udus * 1.35
            self.ucuncu = self.udus * 1.10
            print("Size 10 sans verilecek eger zer gedisiniz tapsaniz sizin udusunuz \n"
                  "1-ci gedisde {} AZN [50%] 2-ci gedisde {} AZN [35%] 3-cu gedisde {} AZN [10%] elave olacaq eks halda uduzacaqsiniz".format(
                self.birinci, self.ikinci, self.ucuncu))
            self.zerler()
        else:
            print('Udus reqem olmalidir ve 0, menfi eded olmaz')
            self.udusu_yoxla()


    def zerler(self):
        self.zer_1_deyeri = int(input("Birinci zerin qiymeti: "))
        self.zer_2_deyeri = int(input("Ikinci zerin qiymeti: "))
        try:
            if self.zer_1_deyeri < 1 or self.zer_1_deyeri > 6:
                print("Zer secimini duzgun edin [1-6] araliginda")
                self.zerler()
            elif self.zer_2_deyeri < 1 or self.zer_2_deyeri > 6:
                print("Zer secimini duzgun edin [1-6] araliginda")
                self.zerler()
            else:
                self.oyuna_basla()
        except ValueError:
            print('Herf olmaz Zer secimini duzgun edin [1-6] araliginda ')
            self.zerler()



    def oyuna_basla(self):
        for i in range(10):
            self.zer_1 = random.randint(1, 6)
            time.sleep(1)
            self.zer_2 = random.randint(1, 6)


            if self.zer_1_deyeri == self.zer_1 and self.zer_2_deyeri == self.zer_2:
                print(f"Siz {i + 1} gedisde tutdugunuz {self.zer_1_deyeri}:{self.zer_2_deyeri} oyunda atilan {self.zer_1_deyeri}:{self.zer_2_deyeri} zeri ile eynidir")
                print('Tebrikler siz uddunuz..')

                if i >= 1 or i <=3:
                    print(f"Sizin udus mebleginiz {self.birinci} AZN")

                elif i  > 3 or i <=6:
                    print(f"Sizin udus mebleginiz {self.ikinci} AZN")

                elif i > 6 or i <=10:
                    print(f"Sizin udus mebleginiz {self.ucuncu} AZN")

                break

            else:
                print(f"{i + 1}-gediw-->Sizin Zer {self.zer_1_deyeri}:{self.zer_2_deyeri} Zer atildi ....{self.zer_1}:{self.zer_2}")
                print('Cox Tesuf Siz uduzdunuz...')
        self.menu()



Zerler()
