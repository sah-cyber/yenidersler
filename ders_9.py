from datetime import *
import time
def qiymet():
    mehsul_dict ={}
    endirim = 40

    for i in range(3):
        mehsullar = input(f'{i+1}. Mehsulu elave edin: ')
        qiymetler = int(input(" hemin mehsulun qiymetini elave edin: "))
        mehsul_dict[mehsullar]=qiymetler

    bu_gun = datetime.now()
    print(bu_gun.strftime('%Y-%m-%d %H:%M:%S'))
    elave_gun = int(input("Endirim nece gunden sonra olacaq : "))

    format_gun = bu_gun + timedelta(days=elave_gun)
    print('*' * 50)

    for k,v in mehsul_dict.items():
        j = v*(1-endirim/100)
        mehsul_dict[k]=j
        print(f"indiki qiymet {k} {v}")
        print(f"endirimli qiymet {k} {j:.02f}")
    print('*' * 50)
    print(f"Sizin elave etdiyini gun sayi  {format_gun.day}/{format_gun.month}/{format_gun.year}-ile duwur")

    print(f"Sizin endirimli günlərə {format_gun.strftime('%Y-%m-%d')} tarixində {elave_gun} gün qaldı.")




qiymet()