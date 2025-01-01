import random
import sys
import time


class Oyuncu:
    def __init__(self,isim,can=5,enerji=100):
        self.can = can
        self.enerji = enerji
        self.isim = isim
        self.zerbe = 0


    def movcud_durumu_goster(self):
        print(f"Adi: {self.isim:>10}\nZerbe: {self.zerbe:>5}\nEnerji: {self.enerji:>5}\nCan: {self.can:>7}")


    def hucum_et(self,duwmen):
        print('Bir hucum heyata kecirin')
        print('Hucum basladi!! Diqqet!!!!')
        for i in range(10):
            time.sleep(1)
            print('.',end=' ',flush=True)

        qerar = self.hucumu_hesabla()

        if qerar == 0:
            print('\nQERAR: Qazanan teref yox')

        if qerar == 1:
            print('\nQERAR: Dusmeni zerbelediniz')
            self.zerbe_endir(duwmen)

        if qerar == 2:
            print('\nQERAR: Dusmen Sizi zerbeledi ')
            self.zerbe_endir()


    def qac(self):
        print('Qacin!!')
        for i in range(10):
            time.sleep(1)
            print('\n',end=' ',flush=True)

        print('\nDusmen sizi tutdu!!')

    def zerbe_endir(self,zerbelenen):
        zerbelenen.zerbe +=1
        zerbelenen.enerji -=10
        print(f"{zerbelenen.isim} enerjisinden 10 cixildi, yeni enerji: {zerbelenen.enerji}")
        if (zerbelenen.zerbe %5)==0:
            zerbelenen.can -=1
            print(f"{zerbelenen.isim} canindan 1 cixildi, yeni can: {zerbelenen.can}")
        if zerbelenen.can <=0:
            zerbelenen.enerji =0
            print("Oyunda {} qalib geldi".format(self.isim))
            self.oyundan_cix()



    def hucumu_hesabla(self):
        return random.randint(0,2)



    def oyundan_cix(self):
        print('Cixdiniz....')
        sys.exit()



siz = Oyuncu('Shahin')

dusmen = Oyuncu('Ehmed')


while True:
    print("""BU an duwmenle qarwi qarwiyayoq.
    Etmek istediyiniz
    'Hucum': 's'
    'Qacmaq': 'k'
    'Cix': 'q'""",sep='\n')

    istek = input('\n==> ').lower()
    if istek == 's':
        siz.zerbe_endir(dusmen)
        print('Duwmenin duwumu')
        dusmen.movcud_durumu_goster()

        print('Sizin Durumunuz')
        siz.movcud_durumu_goster()
    elif istek == 'k':
        siz.qac()

    elif istek == 'q':
        siz.oyundan_cix()

    else:
        print("Yanlis secim etdiniz!")
