import random
import time
class Zerler:

    def __init__(self):
        print('Oyuna xow Gelmisiniz')

        self.list_adlar = ['Aydan', 'Nubar', 'Lale', 'Orxan', 'Cavid']#siradan bir oyuncu adi cixir ekrana
        print(
            '''Zer atisi oyununa xosh gelmisiniz! Oyununa baslamaq ucun 'enter' cixmaq isteyirsinizse 'Q' duymesini basin''')

        self.player = []
        self.gedis = []
        self.pul=[]
        self.control()


    def control(self):
        self.start = input('Seciminiz [ENTER ve ya Q]: ')
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
            self.list_adlar.append(self.adiniz)
            self.udusu_yoxla()
        else:
            print('secimi duzgun edin reqem ve 3 herfden qisa ad olmaz')
            self.ad_yoxla()


    def udusu_yoxla(self):
        self.udus = input("Udusunuzu elave edin..[AZN]: ")
        if self.udus.isdigit() and int(self.udus) > 0:
            print(f"Tewekur edirem '{self.adiniz.capitalize()}' Siz {self.udus} AZN udus meblegi qoydunuz!")
            print('*' * 50)
            self.udus = int(self.udus)
            self.birinci = self.udus * 1.50
            self.ikinci = self.udus * 1.35
            self.ucuncu = self.udus * 1.10
            print("Size 10 sans verilecek eger zer gedisiniz tapsaniz sizin udusunuz \n"
                  "1-ci gedisde {:0.2f} AZN [50%] 2-ci gedisde {:0.2f} AZN [35%] 3-cu gedisde {:0.2f} AZN [10%] elave olacaq eks halda uduzacaqsiniz".format(
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
        self.qalib_gelen = False
        for i in range(50):
            self.zer_1 = random.randint(1, 6)
            time.sleep(1)
            self.zer_2 = random.randint(1, 6)


            if self.zer_1_deyeri == self.zer_1 and self.zer_2_deyeri == self.zer_2:
                print(f"Siz {i} gedisde tutdugunuz {self.zer_1_deyeri}:{self.zer_2_deyeri} oyunda atilan {self.zer_1_deyeri}:{self.zer_2_deyeri} zeri ile eynidir")

                print('Tebrikler siz uddunuz..')
                self.player.append(self.adiniz)



                if i >= 1 or i <=3:
                    print(f"Sizin udus mebleginiz {self.birinci} AZN")
                    self.pul.append(self.birinci)


                elif i  > 3 or i <=6:
                    print(f"Sizin udus mebleginiz {self.ikinci} AZN")
                    self.pul.append(self.ikinci)


                elif i > 6 or i <=10:
                    print(f"Sizin udus mebleginiz {self.ucuncu} AZN")
                    self.pul.append(self.ucuncu)

                self.qalib_gelen = True
                self.gedis.append(i)


                break

            else:
                print(f"{i + 1}-gediw-->Sizin Zer {self.zer_1_deyeri}:{self.zer_2_deyeri} Zer atildi ....{self.zer_1}:{self.zer_2}")
                print('Siz uduzdunuz')
        if not self.qalib_gelen:
            print('Tesuf edirik hec kim qalib gelmeyib')
        self.oyuncu_sirasi()
        self.menu()

    def oyuncu_sirasi(self):

        qalib_list = dict(zip(self.player, zip(self.gedis,self.pul)))
        #print(qalib_list)

        print()
        print('Qalibler')
        print('*'*10)
        print()
        s=0
        for k,v in (qalib_list.items()):
            s+=1
            print(f'{s}. {k.capitalize()} {v[0]} gediwatda {v[1]} AZN uddu!')

        self.sorted_qalibler = sorted(qalib_list.items(),key=lambda x: x[1][1], reverse=True)
        print()
        print('*'*10)
        print()
        print('Top 3-luk')
        print('*'*10)
        for i,play in enumerate(self.sorted_qalibler[:3],start=1):
            print(f"{i}.sirada  {play[0].capitalize()} adli oyuncu  {play[1][0]} gediwata..{play[1][1]} AZN qazandi.")






Zerler()
