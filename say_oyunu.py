import random
import time
print('Say oyununa xow gelmisiniz!')

def say_oy():
    print('Kampyuter 1-den 50 qeder olan say araliginda\n'
          'bir say tutacaq sizin iwiniz hemin ededi tapmaqdir')


    saygac = 5
    kamp_sayi = random.randint(1, 15)
    print(kamp_sayi)

    say_t = []
    while True:
        print('*'*35)
        print("Sizin {} canini var".format(saygac))
        try:
            oyuncu = int(input('Sizi bir say yaziniz:0-15 araliginda:  '))


            if oyuncu <=0 or oyuncu > 15:
                print("Zehmet olmasa 1-15 araliginda reqem girin")
                continue


            if oyuncu in say_t:
                print("BU ededi daha evvel daxil etmisiniz bawqa eded daxil edin: ")
                continue

            say_t.append(oyuncu)
            print(f"Sizin yazdiginiz say {oyuncu}")
            saygac -= 1

            if kamp_sayi == oyuncu:
                print(f"Tebrikler siz sayi tapdiniz {oyuncu} = {kamp_sayi}")
                firework_effect()
                break
            elif oyuncu > kamp_sayi:
                print('Kicik eded dusunun')
            elif oyuncu < kamp_sayi:
                print('Boyuk eded dusunun')

        except ValueError:
            print('Xeta 1-15 araliginda eded yazin')
            continue






        if saygac == 0:
            print('Sizin caniniz qutardi')
            break
        print('*'*35)


def firework_effect():
    fireworks = [
        "🎆 🎆 🎆  Təbriklər! 🎆 🎆 🎆",
        "✨ ✨ 🎇  Siz Qalibsiniz! 🎇 ✨ ✨",
        "🎆 🎇 ✨  Fişənglər Partlayır! ✨ 🎇 🎆",
        "🎉  🎉  Təbriklər! 🎉  🎉",
    ]

    for firework in fireworks:
        print(firework)
        time.sleep(0.5)  # Hər bir fişəngdən sonra 0.5 saniyə gözləyirik


say_oy()