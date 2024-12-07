
#
# soz = 'zeferan'
# #soz = soz.upper()
# #
# # soz = soz.split()
# # print(soz)
# mylist = []
# for s in soz:
#     mylist.append(s.upper())
#    # print(s.upper())
#
# print(mylist)
#



#
# while True:
#     eded = int(input("Enter a number: "))
#     cem = eded +eded
#     print(cem)
#     if eded == 0:
#         break
#
# parol = '12345'
# while True:
#     daxil_et = input('Daxil et: ')
#     if daxil_et == parol:
#         print('Xosh gelmisiniz')
#         break
#     else:
#         print('parol sehfdir')

#
# # tot = 0
#
# for i in range(5):
#     eded = int(input('Enter a number: '))
#     cem = eded **2
#     print(cem)
#
# # print(cem)

# tek = []
# cut = []
# a=1
# while a <= 100:
#
#
#
#     if a%2==0:
#         cut.append(a)
#     else:
#         tek.append(a)
#     a += 1
# print(tek)
# print(cut)

# element = input("elemet araligini qeyd edin ").split()
# print(element)
# birinci = element[0]
# ikinci = element[1]
#
# birinci = int(birinci)
# ikinci = int(ikinci)
#
# fib = []
# for i in range(birinci,ikinci):
#      fib.append(i)


# text = 'python proqlawdirmagi oyrenmek '




# reqem = input("Enter a number: ")
#
# boyukeded = max(reqem)
# cem = 0
#
# for i in reqem:
#     if i != boyukeded:
#         cem +=int(i)
#
# print(cem)
#
#
#
# cem = 0
#
# for i in range(1,101):
#     if i % 2 == 1:
#         cem +=i
#     else:
#         cem -=i
#
# # print(f"1-den 100 qeder olan ededlerin cemi {cem}")
#
# m = int(input("Birinci ededi daxil edin: "))
# n = int(input("Ikinci ededi daxil edin: "))
#
# hasil = 12
# count = 0
# for i in range(m, n+1):
#     if i %3 == 0 and i % 4 == 0:
#         if i % hasil !=0:
#             count += 1
#
# print(f'ededlerin sayi {count}')
#
#

#
# for i in range(1,11):
#     if i == 3 or i == 7:
#         continue
#     else:
#         print(i)
#
# for i in range(1,31):
#     if 5 <= i <=10 or 22 <= i <=28:
#         continue
#
#     print(i)

# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

# i = 0
# saygac = 0
# while i<=10:
#     if i%2 == 0:
#         saygac +=1
#     i+=1
# print(saygac)

# eded = int(input("Enter a number: "))
# cem = 0
# for i in range(eded, eded+10):
#     cem +=i
# orta = cem/10
# print(orta)

# eded = int(input("Enter a number: "))
#
# factorial = 1
# for i in range(1,eded+1):
#     factorial *=i
#
# print(factorial)

# eded = int(input("Enter a number: "))
#
# i = 1
# factorial = 1
#
# while i <= eded:
#     factorial *=i
#     i += 1
#
# print(factorial)

# b=0
# for a in (2,6):
#     while a*a <5*a:
#         a=a+2*a
#         b=a+b
# print(b)



# birinci = float(input("Birinci imtahan neticesi: "))
# ikinci = float(input("Ikinci imtahan neticesi: "))
# ucuncu = float(input("Ucuncu imtahan neticesi: "))
# dorduncu = float(input("Dorduncu imtahan neticesi: "))
#
# cem = (birinci+ikinci+ucuncu+dorduncu)/4
# print(cem)


# for i in range(1,5):
#     print(i)
# print('*'*10)
# i=1
# while i<=4:
#     print(i)
#     i+=1

# i = 1000
# while True:
#     i -=1
#     if i < 0:
#         if i==-1000:
#             print(-i)
#             break
#     if i <-500:
#         if i == -1000:
#             print(i)
#             break


# i = 1000
# while True:
#     i -=1
#     if i < -500:
#         if i==-1000:
#             print(i)
#             break
#     if i < 0:
#         if i == -1000:
#             print(i)
#             break



# i = 1000
# while True:
#     i -=1
#     if i < -500:
#         if i==-1000:
#             print(i)
#             break
#     if i < 0:
#         if i == -1000:
#             print(-i)
#             break


# i = 0
# while True:
#     i+=1
#     if i <=5:
#         print(i,end=' ')
#     else:
#         break


# a = 1
#
# for i in range(1,5):
#     a+=i
#     if a < 10:
#         print(a)
#         break
#
# for i in range(1,4):
#     print(f"{i}-ci qrup")
#     for j in range(1,i+1):
#         print(f"{j}-ci yer")
#

#
# qrup = 1
#
# while qrup <= 3:
#     print(f"{qrup}-ci qrup")
#     yer = 1
#     while yer <= qrup:
#         print(f"{yer}-ci yer")
#         yer +=1
#     qrup += 1
# l=[]
# tot = 0
# for i in range(1,4):
#     eded = float(input('Eded daxil edin: '))
#     l.append(i)
#     tot +=eded
# print(l)
# print(tot)
# l1=[]
# a=0
# while a<3:
#     num = float(input(f'{a+1} Enter a number: '))
#     l1.append(num)
#     a+=1
#
# print(sum(l1))
#

# l= []
# for i in range(3):
#     number = float(input(f"{i+1} Enter a number: "))
#     l.append(number)
# print(min(l))


# l1=[]
#
# a=0
# while a<3:
#     number = float(input(f"{a+1} Enter a number: "))
#     l1.append(number)
#     a=a+1
# print(min(l1))
#
# l=[]
# tot = 0
# for i in range(1,4):
#     eded = float(input('Eded daxil edin: '))
#     l.append(i)
#     tot +=eded
# print(l)
# print(tot/len(l))


# l1=[]
# a=0
# while a<3:
#     num = float(input(f'{a+1} Enter a number: '))
#     l1.append(num)
#     a+=1
# cem = sum(l1)/len(l1)
# print(f"{cem:.2f}")

# print(16**0.5)
# import math
# l=[]
# for i in range(1,16):
#     sqrt = math.sqrt(i)
#     if sqrt.is_integer():
#         l.append(i)
#         print(i)
# print('ededlerin sayi',len(l))
#
# print('*'*20)
# a=1
# l1=[]
# while a<15:
#     sqrt1 = math.sqrt(a)
#     if sqrt1.is_integer():
#         l1.append(a)
#         print(a)
#     a=a+1
# print('ededlerin sayi',len(l1))


# number = int(input("Enter a number: "))
#
# binary_number = bin(number)
# birliyi_tapmaq = binary_number.count('1')
# print(f"verilmis ededlerin ikili sistemde 1 ededlerin sayi {birliyi_tapmaq}")


# num = int(input("Enter a number: "))
#
# if num <=1:
#     print(f"{num} sade eded deyil")
# else:
#     is_prime = True
#
# for i in range(2, num):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f"{num} sade ededir")
# else:
#     print(f"{num}sade eded deyil")


# num = int(input("Enter a number: "))
#
# eded = 0
#
# while num >0:
#     digit=num%10
#     eded +=digit
#     num //=10
#
# print(f"Daxil etdiyiniz ədədin rəqəmlərinin cəmi: {eded}")

# list_ = ["volvo","BMV","Auidi","toyota","Opel"]
# caunt = 0
# for i in list_:
#     if i[0].isupper():
#         caunt+=1
#         print(i)
# print('boyuk herfle bawlayan elementlerin sayi {}'.format(caunt))


# str_ = "lalafo"
#
# print(str_.replace('l','L',2))
#
# deyiw = ''
#
# for char in str_:
#     if char == 'l':
#         deyiw +='L'
#     else:
#         deyiw += char
# str_ = deyiw
# print(str_)

# l = ['nadir','malik','ayxan','ali','leman','lale']
#
# mylist = []
#
# for i in l:
#     if i[0] == 'l':
#         mylist.append(i)
# print(mylist)
# l = ['apple','pear','banana','orange']
#
# for i in range(1,len(l)+1):
#     print(i)

# mylist_ = []
# say = int(input('nece deyisen elave etmek isteyirsiniz: '))
#
# for i in range(1, say + 1):
#     daxil_et = input('liste elave edin: ')
#     mylist_.append(daxil_et)
# len_say = len(mylist_)
#
# for i in range(len_say):
#     print(f'{i+1} Eldar')
# a=1
# s=[]
# while a < 10:
#     if a%2==0:
#         s.append(a)
#         print(a)
#     a=a+1
#
# print(s[:-1])


# t= 2
# counter =1
#
# while t<=10:
#     if counter !=2:
#         print(t)
#     counter+=1
#     t+=2
#
#



# for i in range(20,41):
#     if i % 2 == 0:
#         print(i)
#
#     if i == 38:
#         break


# eded =int(input('Enter a number: '))
#
# if eded >=12:
#     for i in range(eded,1,-1):
#         if i %2 ==0:
#             print(i)
# else:
#     print('Eror')
#
# num = int(input("Enter a number: "))
#
#
# lin_s = len(str(num))
# while num > 0:
#     digit = num //10 ** (lin_s-1)
#     print(digit)
#
#     num = num %10 ** (lin_s-1)
#
#     lin_s = lin_s - 1

# num = int(input("Enter a number: "))
#
# while num > 0:
#     digit = num % 10
#     if digit %2 !=0:
#
#         print(digit)
#
#     num //= 10

# eded = int(input("Enter a number: "))
# counter = 0
# while eded > 0:
#     eded //=10
#
#     counter += 1
#
# print(f'Daxil etdiyiniz ededlerin sayi {counter}')






#
# string = input("Bir string daxil edin: ")
#
# count = 0
# index = 0
#
# while index < len(string):
#     if string[index] == 'a':
#         count += 1
#     index += 1
# print("'a' simvolunun sayi:", count)

# num = int(input("Enter a number: "))
#
# tek =[]
# while num > 0:
#     digit = num % 10
#     if digit % 2 !=0:
#         tek.append(digit)
#     num //=10
# if tek:
#     print(tek)
# else:
#     print('tek eded yoxdur')
#
#


# num = int(input('Enter a number: '))
# number_str = str(num)
# digit = []
# i=0
#
# while i < len(number_str):
#     digiit_ = int(number_str[i])
#     if digiit_ %2 !=0:
#         digit.append(digiit_)
#     i +=1
#
# #digit.sort()
# print(sum(digit))


# text = input("BIr metn daxil edin: ")
# up_say = 0
# i=0
#
# while i<len(text):
#     if text[i].isupper():
#         up_say += 1
#     i+=1
#
# if up_say >0:
#     print('boyuk herflerin sayi',up_say)
# else:
#     print('Boyuk herf yoxdur')


# text = input("Enter a string: ")
# number = int(input("Enter a number: "))
#
# text_length = len(text)
#
# if number < text_length:
#     new_text = text[:number]
#     print('Yeni cumle',new_text)
#
# else:
#     new_text = text + '.'
#     diference = number - text_length
#     print('Yeni cumle:',new_text)
#     print('Ferq:',diference)


# total = 0
#
# while total <100:
#     number = int(input("Enter a number: "))
#     total += number
# print(total)
#
# sait_sesler = "AEƏIOÖUÜaeəioöuü"
# text = input('Enter a sentence: ')
# word = text.split()
#
# for i in word:
#     if i.startswith(sait_sesler) not in sait_sesler:
#         print('Try')
#         break
# else:
#     print('OK')

# mylist = []
# for i in range(3):
#     name = input("Enter your name: ")
#     mylist.append(name)
# print('Listin uzunlugu',len(mylist))


# sait_sesler = "AEƏIOÖUÜaeəioöuü"
#
# text = input('Metn daxil edin: ')
#
# words = text.split()
#
#
# for  word in words:
#     if word[0] not in sait_sesler:
#         print('Baslamir')
#         break
# else:
#     print('Baslayir')
# numbers=[]
#
# for i in range(3):
#
#     number = int(input(f'{i+1}-3 eded daxil edin: '))
#
#     numbers.append(number)
# if len(set(numbers)) == 1:
#     print("Hamisi eynidir")
# elif len(set(numbers)) == 2:
#     print("Ixtiyari ikisi eynidir")
# else:
#     print("Ədədlərin hamısı fərqlidir")


# text = 'k!a%&4@10$2 '
# say =0
# for i in text:
#     if i.isdigit():
#         say +=int(i)
# print('reqemlerin cemi',say)


#
# import re
#
# text ='k!a%&4@10$2 '
# numbers = re.findall(r'\d+', text)
# sum_numbers = sum(int(num) for num in numbers)
# print(f"{' + '.join(numbers)} = {sum_numbers}")


# vowels = "AEƏIOÖUÜaeəioöuü"
#
# # İstifadəçidən ad və soyad daxil etməsini istəyirik
# full_name = input("Ad və soyadınızı daxil edin: ")
#
# # Adı və soyadı ayırırıq
# name_parts = full_name.split()
#
# # Adın ilk hissəsini götürürük
# first_name = name_parts[0]
#
# # Adın bütün hərflərini yoxlayırıq
# for char in first_name:
#     if char not in vowels:  # Əgər hərf sait deyilsə
#         print("Adın bütün hərfləri sait deyil.")
#         break
# else:
#     print("Adın bütün hərfləri saittir.")

# text = 'k!aa%&44@10$2'
#
# dublikat = []
#
# for i in range(1,len(text)):
#     if text[i] == text[i-1]:
#         dublikat.append(text[i])
#
# print('yanasi olan simvollar',dublikat)

# numbers = list(map(int, input("Bir neçə natural ədəd daxil edin, boşluq ilə ayırın: ").split()))
#
# total = 0
#
# for num in numbers:
#     fact = 1
#     i = 1
#     while i <= num:
#         fact *= i
#         i += 1
#     total += fact
#
# print("Ədədlərin faktoriallarının cəmi:", total)


# number = input("Enter a number: ")
#
# tek_eded = 0
# cut_eded = 0
#
# for i in number:
#     if int(i)%2 == 0:
#         cut_eded += 1
#     else:
#         tek_eded += 1
# print(f"Cut Eded: {cut_eded}")
# print(f"Tek Eded: {tek_eded}")


# n = int(input("Siyahida nece element olmagini isteyirsiniz?  "))
# elements = []
#
# for i in range(n):
#     element = int(input(f'{i+1} ededleri daxil ele: '))
#     elements.append(element)
#
# for i in range(1,n,2):
#     elements[i] = elements[i]**2
#
# sum_elements = sum(elements[i] for i in range(0, n, 2))
# print(f"Siyahı: {elements}")
# print(f"Tək indeksli elementlərin cəmi: {sum_elements}")
# Morgan: 90
# Tom :70
# Keen:60
# Raymond:50


# dataset = {"names":{ 1:"Morgan",2:"Tom",3:"Keen",4:"Raymond" },
#             "positions":{ "Morgan":"Producer","Tom":"Manager","Keen":"Accounting","Raymond":"Security Personal" },
#             "scores":{ "Producer":90, "Manager":70, "Accounting":60, "Security Personal":50 } }
#
#
# for id, name in dataset['names'].items():
#     #print(id, name)
#     position = dataset['positions'][name]
#     #print(position)
#     score = dataset['scores'][position]
#     #print(score)
#     print(f"{name}: {score}")
#

#
# for num in range(1,11):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(f"İlk sadə ədəd: {num}")
#             break


# text = input('bir metn daxil edin: ')


# for i,char in enumerate(text):
#     remaining = len(text) - i - 1
#     if remaining > 0:
#         print(f"{char} (daha {remaining} simvol qalib)")
#     else:
#         print(f"{char} (sonuncudur)")



# for i in range(1,101):
#     if i %10 == 3:
#         print(i)

# l = [1,2,3,4]
# let = 'abcd'
#
# for leter,number in zip(let,l):
#     print(f"({leter}, {number})")
#
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [2,3,6,5]
#
# l3=[]
#
# l1=l1+l2
# for i in l1:
#     kv = int(i)**2
#     l3.append(kv)
# print(l3)

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [2,3,6,5]
#
# result = [x**2 for x in l1 if x %2 !=0 and x not in l2]
# print(result)

# [1,2,3,4,5,6,7,8,9,10,11,12] seklinde yazdirin
# l1 = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]
#
# # l2 = [x for i in l1 for x in i]
# # l3=[]
# # for i in l1:
# #     for j in i:
# #         l3.append(j)
# # print(l3)
#
# print(l2)

# number = [1,2,3]
# leters = 'abcd'
# result =[]
# for i in number:
#     for l in leters:
#         result.append([str(i),l])
#
# print(result)
# #result = [[str(n), l] for n in number for l in letters[:3]]
#
# res = [[str(i),l] for i in number for l in leters]
# print(res)


# eded = input('bir eded daxil edin: ')
#
# dogit = sorted(eded)
#
#
# print('<'.join(dogit))

# a = ['apple','pear','pineapple','orange','grape']

# while len(a) >2:
#     a.pop()
# print(a)
# a = ['apple','pear','pineapple','orange','grape']
# b=[]
# index = 0
#
# while index < len(a):
#     if a[index] != 'apple' and a[index] != 'pear':
#
#         print(a[index])
#         b.append(a[index])
#     index += 1
# print(b)
#
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     number = number+number
#     print(number)

# parol_ = '12345'
# parol=''
# while parol != parol_:
#     parol = input('Enter a password: ')
#
# print('Duzdur')
#
# l=[]
# for i in range(5):
#     number = int(input(f"{i+1} Enter a number: "))
#     number = number**2
#     l.append(number)
# print('Verilmis ededlerin kvadratlari ',l)

# li=[]
# i = 0
# while  i<5:
#     number = int(input("Enter a number: "))
#     number = number**2
#     li.append(number)
#     i +=1
# print(li)

# tek = []
# cut = []
# i =1
# while i <= 100:
#     if i % 2 == 0:
#         cut.append(i)
#     else:
#         tek.append(i)
#     i +=1
# print('tek ededler olan list {}'.format(tek))
# print('cut ededler olan list {}'.format(cut))


# n = int(input("Fibonacci ardıcıllığının neçə elementini istəyirsiniz? "))
# a, b = 0, 1
#
# print("Fibonacci Ardıcıllığı:")
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# text = input("bir metn daxil edin: ")
#
# for i in text:
#     if i == ' ':
#         continue
#     print(i,end='')