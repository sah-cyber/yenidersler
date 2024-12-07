

def yoxla():
    print('1::')
    soz = input('Soz elave edin: ')
    if soz.isdigit():
        print('soz reqemlerden ibaretdir')
    elif soz.isalpha():
        print('soz herflerden ibaretdir')
    elif soz.isalnum():
        print('soz hem reqemden hemde herflerden ibaretdir')
    else:
        print('soz herflerden ibaretdir ibaretdir')

yoxla()


prices = [10, 12, 14, 7, 17, 7, 8, 10, 7, 24, 3, 52, 7, 2, 1, 9, 6, 7]
def endirim_et(prices,endirim):
    print('2::')

    yeni_qiymetler = []

    for qiymet in prices:
        if qiymet > 10:
            yeni_qiymet = qiymet *(1-endirim/100)
            yeni_qiymetler.append(yeni_qiymet)
        else:
            yeni_qiymetler.append(qiymet)
    return yeni_qiymetler
endirim = float(input('Endirim et: '))

yeni_prices = endirim_et(prices, endirim)

print('evvelki qiymet',prices)
print('yeni qiymet',yeni_prices)


def sade_eded(yoxla_eded):
    print('3::')
    if yoxla_eded <=1:
        return False

    for i in range(2,int(yoxla_eded**0.5)+1):
        if yoxla_eded%i==0:
            return False

    return True
eded = int(input("Enter a number : "))
if sade_eded(eded):
    print("Yes")
else:
    print("No")

def ededin_kvadrati(n):
    print('6::')

    kvadratlar = [i**2 for i in range(1,n+1)]
    return kvadratlar
kv_eded = int(input('eded daxil edin '))
print('verilen ededin kvadrati',ededin_kvadrati(kv_eded))


def tek_cut(n):
    print('7::')

    if n % 2 == 0:
        print(f'{n} is an even number.')
        return True
    else:
        print(f'{n} is an odd number.')

number = int(input('Enter a number: '))
tek_cut(number)


def her_ededi_yoxla(n):
    print('8::')

    for i in str(n):
        if int(i) % 2 == 0:
            print(f"Daxil edilen {n} reqemindeki  ededler cutdur")
            return False
    print(f"Daxil edilen {n} tekdir")
    return True
tap_number = int(input("Tap number : "))
her_ededi_yoxla(tap_number)


def mal_odenisi():
    print('9::')
    qiymetler = []

    for i in range(1,6):
        qiymet = float(input(f"{i}. malin qiymetlerini daxil edin USD: "))
        qiymetler.append(qiymet)

    umumu_xerc = sum(qiymetler)

    cixaririq = 100


    if umumu_xerc <= cixaririq:
        print('OK')
    else:
        catismayan = umumu_xerc-cixaririq
        print(f'Catismayan: {catismayan}')
mal_odenisi()


def istirak_etmeyen_satt():
    print('10::')

    saat = int(input("Etdiyi Saat: "))

    vaxt = 40

    hesab = vaxt-saat
    print(f"Alinin istirak etmediyi saatlarin miqdari {hesab}")
istirak_etmeyen_satt()


def uc_eded():
    print('11::')
    mylist = []
    for i in range(1,4):
        eded_d = int(input('3 eded daxil edin :'))

        mylist.append(eded_d)
    mylist.sort(reverse=True)
    cem = mylist[0] + mylist[1]  # Ən böyük iki ədədin cəmi

    print(f"Ən böyük iki ədədin cəmi: {mylist[0]} və {mylist[1]} (Cəm: {cem})")


uc_eded()


def uc_eded_qaytar():
    print('12::')
    azdan = []
    coxalan = []


    for i in range(1,4):
        ededler = int(input("Ededler: "))
        azdan.append(ededler)
        azdan.sort(reverse=True)
        coxalan.append(ededler)
        coxalan.sort()
    coxalan = int(''.join(map(str, coxalan)))
    azdan = int(''.join(map(str, azdan)))

    print('coxalan',coxalan)
    print('azalan',azdan)

uc_eded_qaytar()


def ededi_goster_():
    print('13::')
    ededler_ = input('3 reqemli eded daxil edin: ')

    if len(ededler_) == 3 and ededler_.isdigit():
        reqemler = [int(digit) for digit in ededler_]

        print(f"{ededler_} reqemleri {reqemler}")
    else:
        print('Zehmet olmsa 3 reqemli eded girin')

ededi_goster_()


def melumat_goster():
    print('15::')

    info_=input('Info=: ')

    if info_.isdigit():
        print(f'Info = ededdir {info_}')
    elif info_.isalpha():
        print(f'Info=herfdir {info_}')
    elif info_.isalnum():
        print(f'Info=hem eded hem reqem {info_}')
    else:
        print('Secim edin')


melumat_goster()


def mawin_yoxla():
    print('16::')
    list_ = ["volvo", "BMV", "Audi", "Toyota", "Opel"]
    list_ = [car.lower() for car in list_]

    yoxla = input('tapmaq istediyiniz mawinin adini yazin: ')

    if yoxla.isalpha():
        if yoxla in list_:
            print(f"YAzdiginiz {yoxla} masini listede var")
        else:
            print(f"Yazdiginizi {yoxla} masini listede yoxdur")
    else:
        print('Zehmet olmasa herflerden istifade edin')
mawin_yoxla()


def eyni_eded_o():
    print('17::')

    daxil_et = input('ededleri bowluq ile daxil edin ').split()

    if all(eded == daxil_et[0] for eded in daxil_et):
        print('ededler eynidir')
    else:
        print('ededler ferqlidir')

eyni_eded_o()


def eded_to_sozle(n):
    print('18::')

    ones = ["", "bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]
    tens = ["", "on", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doqsan"]
    hundreds = ["", "yüz", "iki yüz", "üç yüz", "dörd yüz", "beş yüz", "altı yüz", "yeddi yüz", "səkkiz yüz",
                "doqquz yüz"]
    #thousands = ["", "min"]

    result = []


    minlik = n // 1000
    if minlik > 0:
        result.append(ones[minlik])
        result.append('min')
    n %= 1000

    yuzluk = n // 100
    if yuzluk > 0:
        result.append(hundreds[yuzluk])
    n %= 100

    onluq = n // 10

    if onluq > 0:
        result.append(tens[onluq])
    n %= 10

    if n > 0:
        result.append(ones[n])

    return ' '.join(result).strip()


n = int(input("Bir ədəd daxil edin (0-9999 arasında): "))
print(eded_to_sozle(n))

def karnizon():
    print('19::')
    import math

    def kombinzon(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


    n = 5
    k = 2
    result = kombinzon(n, k)
    print(f"5 əsasdan 2-nin kombinzonu: {result}")


karnizon()

def uc_reqem_tap():
    print('20::')

    ededler = input('3 ededi daxil et bowluq ile ').split()

    if len(ededler) <=3:

        qowa = int(ededler[0])+int(ededler[1])


        if qowa == int(ededler[2]):
            print('ededlerin cemi beraberdir')
        else:
            print('ededlerin cemi beraber deyil')
    else:
        print('3 ededen artiq yazmayin')


uc_reqem_tap()


def bowluq_qoy():
    print('21::')
    edeler = input('Eded daxil et: ')

    print(' '.join(edeler))

bowluq_qoy()


def ters_eded():
    print('22::')


    ededler = input("Ededler: ")

    if len(ededler) == 2 and ededler.isdigit():
        reqem1= ededler[0]
        reqem2= ededler[1]

        if reqem1 == reqem2:
            print(f"daxil etdiyiniz reqemler {ededler} eynidir")
        elif reqem1 > reqem2:
            print(f"daxil etdiyiniz {ededler} ilk reqemi boyukdur")
        elif reqem1 < reqem2:
            print(f"daxil etdiyiniz eddin 2 reqemi boyuk oldugu ucun 1-ci yazilir {reqem2}{reqem1}")

    else:
        print('Xahiw edirik 2 reqemli eded daxil edin')

ters_eded()


def tam_eded_verilib():
    print('24::')


    tam_eded = input('2 eded Ededi yaz: ')

    if len(tam_eded) == 2 and tam_eded.isdigit():
        if tam_eded[1] == '0':
            tam_eded = tam_eded[0]

        tam_eded = tam_eded[::-1]
        print(tam_eded)
    else:
        print('2 ede girin')

tam_eded_verilib()


def uc_req_tersine():
    print('25::')
    reqem = input('3 reqemli daxil et: ')

    if len(reqem) == 3 and reqem.isdigit():
        sonuncu = reqem[-1]

        qalan = reqem[:-1]

        yeni_reqem = sonuncu + qalan

        print(yeni_reqem)
    else:
        print('3 ededen artiq reqem olmaz')

uc_req_tersine()



def ad_yoxla():
    print('26::')

    ad = 'Wahin'

    for i in range(3):
        ad_gir = input('Dogru adi daxil edin: ')

        if ad_gir == ad.lower():
            print('Dogru ad')
            break
    else:
        print('Ugursuz')

ad_yoxla()


def login():
    print('27::')
    login = 'Wahin'
    passw = '123456'
    cehd = 0
    while cehd < 3:

        login_ = input('Logini daxil edin: ')
        pass_ = input('Passwordu daxil edin: ')

        if login_ == login and pass_ == passw:
            print('xow gelmisiniz')
            break
        elif login_ == login and pass_ != passw:
            print('pasword sehfdir')

        elif login_ != login and pass_ == passw:
            print('login sehfdir')

        else:
            print('Yeniden cehd edin ')

        cehd += 1
    if cehd == 3:
        print('ugursuz')


login()


def text_yoxla():
    print('28::')

    soz = input('Soz daxil edin: ')

    if any(c.isupper() for c in soz) and (c.islower() for c in soz):
        print('dogrudur')
    else:
        print('dogru deyil')

text_yoxla()


def fesil_yoxla():
    print('30::')
    yay = ['iyun', 'iyul', 'avqust']
    yaz = ['mart', 'aprel', 'may']
    payiz = ['sentyabr', 'oktyabr', 'noyabr']
    qis = ['dekabr', 'yanvar', 'fevral']

    ay_daxil_et = input('Ayi daxil edin: ').lower()

    if ay_daxil_et in yay:
        print(f"Daxil etdiyiniz {ay_daxil_et} ayi Yay fesline aiddir")

    elif ay_daxil_et in yaz:
        print(f"Daxil etdiyiniz {ay_daxil_et} ayi Yaz fesline aiddir")

    elif ay_daxil_et in payiz:
        print(f"Daxil etdiyiniz {ay_daxil_et} ayi Payiz fesline aiddir")
    elif ay_daxil_et in qis:
        print(f"Daxil etdiyiniz {ay_daxil_et} ayi Qis fesline aiddir")

    else:
        print("Secimi duzgun edin")

fesil_yoxla()


def hefte_yoxla():
    print('31::')

    hefte_gun= int(input('Heftenin gununu daxil edin: '))

    gunler = {
        1: "Bazar ertəsi",
        2: "Çərşənbə axşamı",
        3: "Çərşənbə",
        4: "Cümə axşamı",
        5: "Cümə",
        6: "Şənbə",
        7: "Bazar"
    }


    if 1 <= hefte_gun <= 7:
        print(gunler[hefte_gun])
    else:
        print('Duzgun gun nomresi daxil edin[1-7] araliginda')

hefte_yoxla()


def iw_gunu():
    print('32::')

    hefte = int(input('heftenin gununu daxil edin: '))

    if 1 <= hefte <= 5:
        print('heftenin is gunudur')
    elif 6 <= hefte <= 7:
        print('heftenin istirahet gunudur')
    else:
        print('secim duzgun edin')

iw_gunu()


def meqale():
    print('33::')

    meqale = input('Meqaleni qeyd edin: ')

    sozler = meqale.split()

    uzun_soz = [soz for soz in sozler if len(soz) >10]

    print(f"Meqalede verilmis en uzun soz {uzun_soz}")

meqale()

def calc(*args):
    print('34::')
    count = len(args)
    elem = args[count-1]
    return count *elem
print(calc(2,2,1,3))


def tam_ve_kesr():
    print('35::')

    eded = float(input('kesirli ededi daxil edin: '))
    tam_hisse = int(eded)
    kesr_hisse = abs(eded-tam_hisse)
    if eded <0:
        tam_hisse = -abs(tam_hisse)

    print(f"Tam hisse {tam_hisse} kesr hisse {round(kesr_hisse,1)}")

tam_ve_kesr()


def factorial(ededler):
    print('36::')
    import math
    cem = 0
    for eded in ededler:
        cem +=math.factorial(eded)
    return cem

def main():
    ededler = list(map(int, input("Natural ədədləri boşluqla ayıraraq daxil edin: ").split()))

    cem = factorial(ededler)

    print(f"Verilen ededlerin faktorial cemi {cem}")

main()


def inner(text):
    print('37::')
    count= 0
    sait = 'aeiouAEIOU'
    for i in text:
        if i in sait:
            count+=1
    return count

def outer():
    text = input('Metni daxil edin: ')
    sait_sesler = inner(text)
    print(f"metinde {sait_sesler} sait ses var")

outer()

pricess = [10, 12, 14, 7, 17, 7, 8, 10, 7, 24, 3, 52, 7, 2, 1, 9, 6, 7]
def qiymet_endirim(prices):
    print('38::')

    price = float(input('Endirim faizini yazin: '))

    update_price = []
    for i in prices:
        if i >10:
            disc_price = price * (1 - price / 100)
            update_price.append(disc_price)
        else:
            update_price.append(i)
    print('yeni qiymetler ',update_price)


qiymet_endirim(pricess)

def iner(number):
    print('39::')
    if number % 2 == 0:
        return 'cut'
    else:
        return 'tek'

def outer():
    try:
        number = int(input('Enter a number: '))
        result = iner(number)
        print(f"Daxil etdiyiniz ədəd {result} ədəddir.")
    except ValueError:
        print("Zəhmət olmasa düzgün bir ədəd daxil edin.")

outer()

def ucle_biten():
    print('40::')
    count = 0
    for i in range(1,101):
        if i % 10 ==3:
            count = count + 1
    return count

result = ucle_biten()

print(f"100 ededin icinde {result} 3 ile bitir")


def yeddi_bawla():
    print('41::')
    count = 0
    for i in range(1, 101):

        if str(i).startswith('7'):
            count += 1
    return count


result = yeddi_bawla()
print(f"100 ededin icinde {result} 7 ile bawlayir ")


def sual_42():
    print('42::')
    s = 0
    for i in range(1, 100):

        if i % 10 == 3:
            s = s + 1
    print(s)


sual_42()

def kub_sum(number):
    print('43::')
    a = number // 100
    b = (number // 10) % 10
    c = number % 10

    return number == a**3 + b**3 + c**3

valid_n =[]

for i in range(100,1001):
    if kub_sum(i):
        valid_n.append(i)

print(f"Bu şərti ödəyən 3-cədədli saylar: {valid_n}")


def calcualte(users):
    print('44::')
    total_age = 0
    total_user = len(users)
    for user in users:
        total_age += user[1]

    ortalame = total_age / total_user

    return ortalame

ortalame = calcualte(users)

print(f'ortalama yas {ortalame}')

def sade_cut():
    print('45::')
    cut_reqemler = []

    for i in range(100,1000):
        ilk_reqem = i / 1000
        son_reqem = i%10

        if ilk_reqem % 2 !=0 and son_reqem %2 ==0:
            cut_reqemler.append(i)
    return cut_reqemler
print(sade_cut())