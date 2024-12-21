
import os

def elave_10():

    papka_ad = input('Papkanin adini qeyd edin: ')

    if papka_ad[0].isdigit() or len(papka_ad) >=15:
        print('Papka adi reqemle ve 15 simvoldan uzun ola bilmez')

    else:
        os.mkdir(papka_ad)
        print(f"{papka_ad} papkasi ugurla yaradildi")



        fayl_yarat = input('faylin adini qeyd edin :')
        fayl_yarat +='.txt'

        with open(fayl_yarat,'w') as fayl:
            elave_et = input('fayla elaveler edin: ')
            setir = elave_et.splitlines()
            for st in setir:
                fayl.write(st + '\n')

        print(f"{fayl_yarat} faylina sizin metn elave edildi")

        with open(fayl_yarat,'r') as fayl:
            print(fayl.read())

    print(f"{fayl_yarat} faylini silmek isteyirsiniz 'q' duymesini eks halda enter duymesini basin")

    secim = input('seciminiz: ')

    if secim.lower() == 'q':
        os.remove(fayl_yarat)
        print(f"{fayl_yarat} ugurla silindi")
    print(f"{papka_ad} silmek isterdinizse q duymesini basin ")
    papka_secim = input('Secim :')

    if papka_secim.lower() == 'q':
        os.rmdir(papka_ad)
        print(f"{papka_ad} ugurla silindi")





elave_10()