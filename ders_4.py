
class Ders_5:
    def __init__(self):
        self.task_1()




    def task_1(self):
        print('1::')
        num = int(input("Enter a number: "))

        if num > 0:
            print('{} ededi musbet ededir'.format(num))
        elif num < 0:
            print('{} ededi menfi ededir'.format(num))

        else:
            print('{} ededidir'.format(num))

        print('2:')

        num_1 = int(input("Enter a number: "))

        if num_1 % 2 == 0:
            print(f"{num_1} bu eded cut ededir.")
        else:
            print(f"{num_1} bu eded tek ededir")

        print('3:')
        print('3 eded daxil edin')
        mylist = []
        print(mylist)
        for i in range(3):
            number_ = int(input("Ededler: "))
            mylist.append(number_)
        print('ededlerin en boyuyu', max(mylist))

        print('4::')
        user = 'shahin'
        passw = '12345'

        user_ = input('Loginizi daxil edin: ')
        pass_ = input('Passwordu daxil edin: ')

        if user_ == user and pass_ == passw:
            print('Xos gelmisiniz')
        else:
            print('Oops! Girise icazeniz yoxdur')

        print('5:')

        ceki = float(input('Cekinizi daxil edin: '))

        boy = float(input('Boyunuzu daxil edin: '))

        cixaris = ceki / (boy ** 2)

        if cixaris < 18.5:
            kateqoriyaniz = 'Sizin Zeif cekiniz var'

        elif 18.5 <= cixaris < 24.9:
            kateqoriyaniz = 'Normal cekiniz var'

        elif 25 <= cixaris < 29.9:
            kateqoriyaniz = 'KOKsunuz'

        else:
            kateqoriyaniz = 'Obezsiz'

        print(f"Sizin daxil etdiyiniz boyunuza gore kategoriyaniz {kateqoriyaniz}")

        print('6::')
        sait_sesler = 'aeəiıoöuü'

        oz = input("Herfi daxil edin: ")

        if len(oz) > 1:
            print('yalniz bir herf daxil edin')

        elif oz in sait_sesler:
            print('Bu sait sesdir')
        else:
            print('Bu samit sesdir')


        print('7::')
        print('Kalkulyator')

        kontrol = '1234567890-+*/'

        eded = input(':>> ')
        print(eded)

        for i in eded:
            if i not in kontrol:
                print(f"Iceze verilmemis emeliyyat,Ancaq riazi emeliyyat aparin")
                break
        else:
            cem = eval(eded)
            print('Netice', cem)

        print('8::')
        soz = input('Soz daxil edin: ')

        soz = soz.replace(' ', '').lower()

        if soz == soz[::-1]:
            print(soz, 'sozu Polidromdur')
        else:
            print(soz, 'sozu Polidrom deyil')

        print('9::')
        yaw = input('Zehmet olmasa yasinizi daxil edin: ')

        if yaw.isdigit():
            yaw = int(yaw)

            if yaw >= 18:
                print('Sizin ses verme huwunuz var ')
            else:
                print("Sizin sesverme huququnuz yoxdur")
        else:
            print('Reqemden istifade edin')

        print('10::')

        bal = input('Balinizi daxil edin : ')

        if bal.isdigit():

            bal = int(bal)
            if bal > 100 or bal <= 0:
                print('bele bal movcud deyil')
            elif bal >= 90 and bal <= 100:
                print('Sizin kecid baliniz A')
            elif bal <= 89 and bal >= 60:
                print("Sizin baliniz B")

            elif bal <= 59 and bal >= 50:
                print('Sizin bal C')
            else:
                print("Siz qebul olmadiniz")

        print('11::')
        il = int(input("ILi daxil edin: "))

        if (il % 4 == 0 and il % 100 != 0) or (il % 400 == 0):
            print("BU il 366 gunden ibaretdir")

        else:
            print("Bu il 365 gunden ibaretdir")

        print('12::')
        yawiniz = int(input("Yawinizi daxil edin: "))

        if yawiniz <= 0:
            print('OPPS Siz anadan olmamisiniz ')
        elif yawiniz <= 13 and yawiniz >= 5:
            print("Usaqlara bilet 5 Azndir")
        elif yawiniz >= 14 and yawiniz <= 17:
            print('Yeniyetmelere bilet 6 azndir')
        elif yawiniz >= 18 and yawiniz < 99:
            print("Bilet qiymeti 10 azndir")
        else:
            print('Sizin ucun bilet movcud deyil')

        print('13::')
        zaman = int(input('saati daxil edin 24 satliq rejimle yeni axwam saat 6 disa bunu 18 kimi qeyd edin'))
        if 6 <= zaman < 12:
            print('Sabahiniz xeyir')

        elif 12 <= zaman < 18:
            print('Gunortaniz xeyir')
        else:
            print('Axwaminiz xeyir')

        print('14::')

        qiymet = float(input('Aldiginiz malin deyerini qeyd edin: '))

        if qiymet <= 50:
            print('Sizin aliwiniza endirim yoxdur')
        elif qiymet >= 51 and qiymet <= 100:
            print(f'size 10% endrim var {qiymet * 0.9:.2f}')
        elif qiymet > 100:
            print(f'size 20% endirim var {qiymet * 0.8:.2f}')
        else:
            print("Secim edin")


        print('16::')

        eded = input('ededler daxil edin: ')

        cavab = int(eded[0])

        # cavab=int(cavab)

        if cavab % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab} tekdir")

        print('17::')

        eded = input('ededler daxil edin: ')

        cavab = int(eded[1])

        # cavab=int(cavab)

        if cavab % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab} tekdir")

        print('18::')

        eded = input('ededler daxil edin: ')

        cavab = int(eded[-1])

        # cavab=int(cavab)

        if cavab % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab} tekdir")

        print('19::')

        eded = input('ededler daxil edin: ')

        cavab = int(eded[0]) + int(eded[1])
        print(cavab)

        # cavab=int(cavab)

        if cavab % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab} tekdir")

        print('21::')
        eded = input('ededler daxil edin: ')

        cavab = int(eded[0])
        cava1 = int(eded[1])
        print(cavab, cava1)

        # cavab=int(cavab)

        if cavab % 2 == 0 and cava1 % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab}{cava1} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab}{cava1} tekdir")


        print('22::')
        eded = input('ededler daxil edin: ')

        cavab = int(eded[-1])
        cava1 = int(eded[-2])
        print(cavab, cava1)

        # cavab=int(cavab)

        if cavab % 2 == 0 and cava1 % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab}{cava1} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab}{cava1} tekdir")


        print('23::')
        eded = input('ededler daxil edin: ')

        cavab = int(eded[0])
        cava1 = int(eded[-1])
        print(cavab, cava1)

        # cavab=int(cavab)

        if cavab % 2 == 0 and cava1 % 2 == 0:
            print(f"ededinizi ilk reqemi {cavab}{cava1} cutdur")
        else:
            print(f"ededinizi ilk reqemi {cavab}{cava1} tekdir")


        print('24::')
        eded = input('ededler daxil edin: ')
        print(len(eded))
        if 100 <= int(eded) <= 999:
            cavab = int(eded[0])
            cava1 = int(eded[-1])
            print(cavab, cava1)

            if cavab % 2 == 0 and cava1 % 2 == 0:
                print(f"ededinizi ilk reqemi {cavab}{cava1} cutdur")
            else:
                print(f"ededinizi ilk reqemi {cavab}{cava1} tekdir")
        else:
            print('eded 3 reqemli deyil')


        print('26::')

        eded = input('reqemler yazin: ')
        print(eded)

        mylist = []

        mylist.append(eded)

        for i in mylist:
            print('en boyuk eded', max(i))

        print('27::')
        mylist = []
        for i in range(5):
            eded = int(input("Enter a number: "))
            mylist.append(eded)
        print(mylist)
        print('minumum eded', min(mylist))

        print('28::')
        l = ['nadir', 'malik', 'ayxan', 'ali']

        ad = input('Ad daxil edin: ')

        if ad in l:
            print('Bu telebe adi qrupdadir')
        else:
            print('bu telebenin adi qrupda deyil')

        print('29::')
        eded = int(input("Enter a number: "))

        number = list(range(1, eded + 1))
        print(number)
        first_num = number[0]
        last_num = number[-1]

        if first_num < 50 and last_num < 50:
            result = sum(x ** 2 for x in number)
        else:
            result = sum(number)

        print(f"Netice {result}")

        print('30::')

        N = int(input("2-dən böyük bir natural ədəd daxil edin: "))


        if N > 2:
            previous_even = N - 1 if (N - 1) % 2 == 0 else N - 2
            print("N-dən əvvəlki cüt ədəd:", previous_even)
        else:
            print("Xahiş edirik, 2-dən böyük bir ədəd daxil edin.")


        print('31::')

        eded = int(input("Enter a number: "))

        if eded % 6 == 0:
            print('he')
        else:
            print('Yox')

        print('32::')
        print('''y x-den kicikdir 
                y 10-dan kicikdir''')

        print('33::')
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        if age < 18:
            print('Sizin suruculuk vesiqesi almaga yasiniz catmir!')
        else:
            print('Suruculuk vesiqesini ala bilersiz.')

        surucu_v = int(input("surucu vesiqesi ilini yaz: "))
        il = 2026
        surucu_v += 5
        print(surucu_v)
        if surucu_v <= 2026:
            print('suruculuk vesiqesinin vaxtina var')
        else:
            print('Suruculuk vesiqesi vaxti bitib')

        print('34::')
        print('Cinemaya xosh gelmisiniz zehmet olmasa adinizi ve odenis edin')
        name = input('Name: ')
        price = int(input('Price: '))
        print(f'Xosh Gelmisiniz {name},sizin odenisiniz {price} azndir gozleyin secim edilir')
        birinci_yer = 20
        ikinci_yer = 20 * (20 / 100)
        # print(ikinci_yer)
        ucuncu_yer = 20 * (40 / 100)
        # print(ucuncu_yer)
        if price >= birinci_yer:
            print('Size birinci sirada yer verildi')
        elif price == ikinci_yer or price > ucuncu_yer:
            print('Size ikinci yer teklif olundu')
        elif price == ucuncu_yer or price < ikinci_yer:
            print('Size ucuncu yer teklif olundu')
        else:
            print('gozleyin')

        print('35::')
        numbers = list(map(int, input("Rəqəmləri daxil edin (məsələn, 1 2 3 4 5): ").split()))

        # Rəqəmlərin sayını hesablamaq üçün 'Counter' istifadə edirik
        from collections import Counter

        # Rəqəmlərin sayını hesablamaq
        count = Counter(numbers)

        # Təkrarlanan rəqəmləri tapırıq
        duplicates = [num for num, cnt in count.items() if cnt > 1]

        # Nəticəni ekrana çıxarırıq
        if duplicates:
            print("Təkrarlanan rəqəmlər:", duplicates)
        else:
            print("Təkrarlanan rəqəm yoxdur.")

        print('elave')
        mylist = []
        dubl = []

        for i in range(1, 6):
            eded = int(input("Enter a number: "))
            mylist.append(eded)
        print(mylist)

        for i in mylist:
            if mylist.count(i) > 1 and i not in dubl:
                dubl.append(i)

        if dubl:
            print('tekrar', dubl)
        else:
            print('tekrar eded yoxdur')


        print('35::')
        qiymet = float(input('Telefonun qiymetini daxil edin: '))

        faizler = 12 / 100

        total = qiymet * (1 + faizler)

        print(f"12 aylıq faizlə ödəniləcək ümumi məbləğ: {total:.2f} AZN")


Ders_5()