class Ders_1:
    def __init__(self):
        self.menu()

    def menu(self):

        self.word = input('Verilmis Taskin cavabinin tapin: "TASK" N=: ')

        if self.word == '1':
            self.task1()
        elif self.word == '2':
            self.task_2()
        elif self.word == '3':
            self.task_3()
        elif self.word == '4':
            self.task_4()
        elif self.word == '5':
            self.task_5()
        elif self.word == '6':
            self.task_6()
        elif self.word == '7':
            self.task_7()
        elif self.word == '8':
            self.task_8()
        elif self.word == '9':
            self.task_9()
        elif self.word == '10':
            self.task_10()
        elif self.word == '11':
            self.task_11()
        elif self.word == '13':
            self.task_13()
        elif self.word == '14':
            self.task_14()
        elif self.word == '15':
            self.task_15()
        elif self.word == '16':
            self.task_16()
        elif self.word == '17':
            self.task_17()
        elif self.word == '18':
            self.task_18()
        elif self.word == '19':
            self.task_19()
        elif self.word == '20':
            self.task_20()
        elif self.word == '21':
            self.task_21()
        elif self.word == '22':
            self.task_22()
        elif self.word == '23':
            self.task_23()
        elif self.word == '24':
            self.task_24()
        elif self.word == '25':
            self.task_25()
        elif self.word == '26':
            self.task_26()
        elif self.word == '27':
            self.task_27()
        elif self.word == '28':
            self.task_28()
        elif self.word == '29':
            self.task_29()
        elif self.word == '30':
            self.task_30()
        elif self.word == '31':
            self.task_31()
        elif self.word == '32':
            self.task_32()
        elif self.word == '33':
            self.task_33()
        elif self.word == '34':
            self.task_34()
        elif self.word == '35':
            self.task_35()
        elif self.word == '36':
            self.task_36()
        elif self.word == '37':
            self.task_37()
        elif self.word == '38':
            self.task_38()
        elif self.word == '39':
            self.task_39()
        elif self.word == '40':
            self.task_40()
        elif self.word == '41':
            self.task_41()
        elif self.word == '42':
            self.task_42()
        elif self.word == '43':
            self.task_43()
        elif self.word == '44':
            self.task_44()
        elif self.word == '45':
            self.task_45()
        elif self.word == '46':
            self.task_46()
        elif self.word == '47':
            self.task_47()
        elif self.word == '48':
            self.task_48()
        elif self.word == '49':
            self.task_49()
        elif self.word == '50':
            self.task_50()
        elif self.word == '51':
            self.task_51()
        elif self.word == '52':
            self.task_52()
        elif self.word == '53':
            self.task_53()
        elif self.word == '54':
            self.task_54()
        elif self.word == '55':
            self.task_55()
        elif self.word == '56':
            self.task_56()
        elif self.word == '57':
            self.task_57()
        elif self.word == '58':
            self.task_58()

        elif self.word == '59':
            self.task_59()
        elif self.word == '60':
            self.task_60()
        elif self.word == '61':
            self.task_61()
        elif self.word == '63':
            self.task_63()
        elif self.word == '64':
            self.task_64()
        elif self.word == '65':
            self.task_65()
        elif self.word == '66':
            self.task_66_68()
        elif self.word == '69':
            self.task_69_74()
        elif self.word == '75':
            self.task_75_87()
        elif self.word == '88':
            self.task_88()
        elif self.word == '92':
            self.task_92_93()
        elif self.word == '94':
            self.task_94_96()
        elif self.word == '97':
            self.tast_97()
        elif self.word == '98':
            self.task_98()
        elif self.word == '99':
            self.task_99()
        elif self.word == '100':
            self.task_100()
        elif self.word == '101':
            self.task_101()
        elif self.word == '102':
            self.task_102()
        elif self.word == '103':
            self.task_103()
        elif self.word == '106':
            self.task_106()
        elif self.word == '107':
            self.task_107()
        elif self.word == '116':
            self.task_116_118()
        elif self.word == '119':
            self.task_119()
        elif self.word == '125':
            self.task_125()
        else:
            print('Eror- Secimi reqemle edin ve 1 den baslayin')

    def task1(self):
        print('Sual: Print the first digit of the number 2347')
        self.a = 2347
        print(self.a)

    def task_2(self):
        print('Print the second digit of the number (2347 ededinin ikinci reqemini cap edin)')
        a = 2347
        print(a // 100 % 10)

    def task_3(self):
        print('Task3: Print the third digit of the number. (2347 ededinin üçüncü reqemini cap edin)')
        self.a = 2347
        print(self.a // 10 % 10)

    def task_4(self):
        print('Print the last digit of the number. (2347 ededinin son reqemini cap edin) (edited)')
        self.a = 2347
        print(self.a % 10)

    def task_5(self):
        print('Print the number 234 from 2347. (2347 ededinden 234 ededini cap edin) (edited)')
        self.a = 2347
        print(self.a // 10)

    def task_6(self):
        print('Print the number 347 from 2347. (2347 ededinden 347 ededini cap edin) (edited)')
        self.a = 2347
        print(self.a % 1000)

    def task_7(self):
        print('Print the number 47 from 2347. (2347 ededinden 47 ededini cap edin) (edited)')
        self.a = 2347
        print(self.a % 100)

    def task_8(self):
        print("""What will the given code 'print("10000".isnumeric())' return for us? 
        (print("10000".isnumeric()) bize ne verecek?)'""")
        print('10000'.isnumeric())
        print('True sozunu ')

    def task_9(self):
        print("""What will the below code snippet output? (Asaqidaki code snippeti bize ne dondurecek?)""")
        self.str2 = 'pythyony'
        print(self.str2.find('y', 5, 8))
        print('7 reqemini')

    def task_10(self):
        print("""What "/" in Python means? (Pythonda "/" ne ifade edir? )""")
        print('ededlerde bolme islerini ve hemcinin xusisi simvollari deaktiv etmek ve yeni setire kecmek ucun')

    def task_11(self):
        print('''What "//" in Python means? (Pythonda "//" ne ifade edir? )''')
        print("Ededi tam bolur")
        print('''What "%" in Python means? (Pythonda "%" ne ifade edir? )''')
        print('Ededin qaligini gosterir')

    def task_13(self):
        print('''What will the below code snippet output? (Asaqidaki code snippeti bize ne dondurecek?)''')
        self.str2 = 'worldheyhello'
        print(self.str2.count('h'))
        print('h herfinin sozde kecen toplamini')

    def task_14(self):
        print('''What will the below code snippet output? (Asaqidaki code snippeti bize ne dondurecek?)''')
        self.str1 = 'poython'
        print(self.str1.replace('o', '', 1))
        print('sozde kecen 1-ci "o" herfini bowluqla evez edir')

    def task_15(self):
        self.str1 = 'poython'
        print(self.str1.replace('o', '', 2))
        print('sozde kecen "o" herfleini bowluqla evez edir')

    def task_16(self):
        print('''str_ = Replace the 'e' character in the string 'kenan" 'e' with 'a and the 'a' character with 'o'." 
        (kenan" stringinde e characterini a ile , a characterini ise o ile evez edin)''')
        self.str1 = 'kenan'
        print(self.str1.replace('e', 'a', ), self.str1.replace('a', 'o', 1))

    def task_17(self):
        self.a = 2357
        print('''Assign 2357 number to a variable then calculate the sum of the second and third elements of the number.
         (2357 ededini bir deyisene menimsedin ardindan verilmis ededin ikinci ve ucuncu reqemlerinin cemini hesablayin)''')
        print((self.a // 10 % 10) + (self.a // 100 % 10))

    def task_18(self):
        print('''Imagine you are given the integer 1247. Calculate the sum of its first and last digits. 
        (int_ = 1247 verilmis ededin ilk ve son reqemlerinin cemini hesablayin)''')
        self.a = 1247
        print((self.a // 1000) + (self.a % 10))

    def task_19(self):
        print('''Imagine you are given the integer 1247. Calculate the sum of its last three digits.
         (int_ = 2347 verilmis ededin son uc reqeminin cemini hesablayin)''')
        self.a = 2347
        print((self.a // 100 % 10) + (self.a % 100 // 10) + (self.a % 100 % 10))

    def task_20(self):
        print('''2347 verilmis ededin ilk 3 reqeminin cemini hesablayin''')
        self.a = 2347
        print((self.a // 1000) + (self.a // 100 % 10) + (self.a // 10 % 10))

    def task_21(self):
        print('''2347 verilmis ededin butun reqeminin cemini hesablayin''')
        a = 2347
        print((self.a // 1000) + (self.a // 1000) + (self.a // 100 % 10) + (self.a // 10 % 10))

    def task_22(self):
        print('''(int = 2347 ededinin 3-cu reqeminin ikinci reqemine bolunmasinden alinan qaliqi tapin)''')
        self.a = 2347
        print((self.a % 100 // 10) // (self.a // 100 % 10))

    def task_23(self):
        print('''"acampschool" stringinde ilk characteri boyuk qalan characterleri kicik herfle yazdirin''')
        self.str_ = "acampschool"
        print(self.str_.capitalize())

    def task_24(self):
        print('''Task24: str_ = "ACAMPSCHOOL" stringinde ilk bes characteri kicik, 
        qlan characterleri boyuk herfle yazdirin''')
        self.str_ = "ACAMPSCHOOL"
        print(self.str_.lower()[:5] + self.str_.upper()[5:])

    def task_25(self):
        print('''Task25: str = "ACAMPSCHOOL" Print the first five characters in uppercase 
        and the remaining characters in lowercase in the string "ACAMPSCHOOL. 
        (str = "ACAMPSCHOOL" stringinde ilk bes characteri boyuk, qalan characterleri kicik herfle yazdirin)''')
        self.str_ = "ACAMPSCHOOL"
        print(self.str_.upper()[:5] + self.str_.lower()[5:])

    def task_26(self):
        print('''Task26: Print all characters in lowercase str = "ACAMPSCHOOL" 
        (str = "ACAMPSCHOOL" stringinde butun characterleri kicik herfle yazdirin)''')
        self.str_ = "ACAMPSCHOOL"
        print(self.str_.lower())

    def task_27(self):
        print('''str_ = "hello world" print(str_[:5])''')
        self.str_ = "hello world"
        print(self.str_[:5])

    def task_28(self):
        print('''str_ = "hello world" print(str_[:5])''')
        self.str_ = "hello world"
        print(len(self.str_))

    def task_29(self):
        print('''str_ = "hello world" sətrini hw sətri kimi cap edin''')
        self.str_ = "hello world"
        print(self.str_[0] + self.str_[6])

    def task_30(self):
        print('''str_ = "hello world" səstrini hlowrd kimi cap edin''')
        self.str_ = "hello world"
        print(self.str_[0] + self.str_[3] + self.str_[4] + self.str_[6] + self.str_[8] + self.str_[-1])

    def task_31(self):
        print('''Task31: str_ = "hello world" sətrini hlwl kimi cap edin''')
        self.str_ = "hello world"
        print(self.str_[0] + self.str_[2] + self.str_[6] + self.str_[9])

    def task_32(self):
        print('''Asaqidaki kodun neticesi ne olacaq?''')
        self.sample = 'Tunar'
        print(self.sample[0].lower() + self.sample[1:].upper())

    def task_33(self):
        self.sample = 'Tunar'
        print(self.sample[0].lower())

    def task_34(self):
        print('''TunarTunar''')
        self.sample = 'Tunar'
        print(self.sample * 2)
        print(self.sample + self.sample)

    def task_35(self):
        print('''TunarranuT''')
        self.sample = 'Tunar'
        self.res = list(reversed(self.sample))
        print(self.sample + ''.join(self.res))

    def task_36(self):
        self.sample = 'Tunar'
        print(self.sample[1:4])

    def task_37(self):
        self.str1 = 'Hello'
        self.str2 = 'World'
        print(self.str1 + self.str2)

    def task_38(self):
        print('''Task38:str_ = "mansur" stringinde n simvolunu ğ ilə, s simvolunu isə d ilə əvəz edib cap edin''')
        self.str_ = "mansur"
        print(self.str_.replace('n', 'ğ').replace('s', 'd'))

    def task_39(self):
        print('''str_ = "mansur"print(str_.replace('n','ğ').replace('s','d'))''')
        self.str_ = "acampschool"
        print(self.str_.count('a'))

    def task_40(self):
        print('''Task40: str_ = "acampschool" stringinde saitlerin cemini hesablayan python kodu yazin''')
        self.str_ = "acampschool"

        self.saitsesler = 'ao'
        self.cem = 0
        for i in self.str_:
            if i in self.saitsesler:
                self.cem += 1
        print(self.cem)

    def task_41(self):
        print('''Task 41: str_ = "acampschool" stringinde o simvollarini hesablayan python kodunu yazin''')
        self.str_ = "acampschool"
        print(self.str_.count('o'))

    def task_42(self):
        print('''Task42: Nə çap olunacaq?''')
        self.str_ = 'pytho'
        self.str_ = self.str_ + 'n'
        print(self.str_[-1].upper())

    def task_43(self):
        print('''Task43: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_.startswith('a'))

    def task_44(self):
        print('''Task44: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_.endswith('oL'))

    def task_45(self):
        print('''Task45: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'

        print(self.str_[len(self.str_) // 2])

    def task_46(self):
        print('''Task46: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[len(self.str_) - 3])

    def task_47(self):
        print('''Task47: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[len(self.str_) % 2])

    def task_48(self):
        print('''Task48: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[len(self.str_) % 11])

    def task_49(self):
        print('''Task49: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[::2])

    def task_50(self):
        print('''Task49: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[::-2])

    def task_51(self):
        print('''Task49: Ne cap olunacaq?''')
        self.str_ = 'Acampschool'
        print(self.str_[0:11:2])

    def task_52(self):
        print('''Task52: "Men python oyrenirem" setrini kommente almaq ucun hansi isareden istifade edilir?''')
        print(" '#' iwaresinden ")

    def task_53(self):
        print('''Task53: len funksiyasi ne ucun istifade edilir?''')
        print("stringin uzunlugunu")

    def task_54(self):
        print(r"""Task54: Yazini cap ederken 3 whitespace yazmaq ucun hansi isareden istifade edilir? \n \t end=""" "")
        print(r"""\t""")

    def task_55(self):
        print("Task55: Novbeti yazini yeni setirden yazmaq ucun hansi koddan istifade edilir?")
        print(r"""\n""")

    def task_56(self):
        print('acampschool sozu Acampschool cap edilsin ')
        self.str_ = 'acampschool'
        print(self.str_.capitalize())

    def task_57(self):
        print('Task57: aba setrinden istifade etmekle terminalda abaabaaba yazisini almaq ucun python kodunu yazin')
        self.str_ = 'aba'
        print(self.str_ * 3)

    def task_58(self):
        print('''Change the positions of the first and last characters in the string 
        'str = 'python'' and print it (str = 'python' setirinde ilk ve son simvollarin yerini deyisib cap edin) ''')
        self.str_ = 'python'
        print(self.str_.replace('p', 'n', 1), self.str_.replace('n', 'p'))

    def task_59(self):
        print('''Find the sum of the second and third digits of the number 
        'ab = 2356'. (ab = 2356 ededinin ikinci ve ucuncu reqemlerinin cemini hesablayin''')
        self.ab = 2356
        print((self.ab // 100 % 10) + (self.ab // 10 % 10))

    def task_60(self):
        print('''Task 60: Take a variable and assign an integer to it, 
        then find its square root. (Bir deyisen goturub ona bir integer menimsedib kokunu tapin) ''')
        self.int_ = 16
        print(self.int_, 'Ededinin koku', self.int_ ** 0.5)

    def task_61(self):
        print('''int1 = 2346 Take the third digit of the above number then raise it to the power
         of the second digit of the same number ( int1 = 2346 Yuxaridaki ededin ikinci reqemini alib esas,
          ucuncu reqemini alib onun quvveti yazib neticeni cap edin) ''')
        self.int1 = 2346
        print((self.int1 // 100 % 10) ** 2)
        print((self.int1 % 100 // 10) ** 2)

    def task_63(self):
        print('''Task63: int_ = 25734 ededinin sondan ikinci reqemini cap edin ''')
        self.int_ = 25734
        print(self.int_ % 100 // 10)

    def task_64(self):
        print('''int_ = 25734 ededinin sondan ucuncu reqemi ile sonuncu reqeminin ferqini tapin''')
        self.int_ = 25734
        self.int1 = self.int_ % 1000 // 100
        self.int2 = self.int_ % 10

        if self.int1 > self.int2:
            print("boyukdur")
        else:
            print('kicikdir')
        print(self.int_ % 1000 // 100)
        print(self.int_ % 10)

    def task_65(self):
        print('''Task65: int_ = 25734 ededinin saqdan ikinci ve soldan ikinci reqemlerinin hasilini hesablayin''')
        self.int_ = 25734
        print((self.int_ % 100 // 10) / (self.int_ // 1000 % 10))

    def task_66_68(self):
        print('''Task66: int_ = 123456 ededinin len methodundan istifade etmekle ilk 3 reqemini (123 seklinde) yazdirin
                Task67: int_ = 123456 ededinin len methodundan istifade etmekle son 3 reqemini (456 seklinde) yazdirin
                Task68: int_ = 123456 ededini 1 reqem oturmekle (135 seklinde) yazdirin
                ''')
        self.int_ = 123456
        self.int_ = str(self.int_)
        print(len(self.int_))
        print(self.int_[:3])
        print(self.int_[3:])
        print(self.int_[::2])

    def task_69_74(self):
        print('''Task69: test = "pythononon" stringinde 3 ve sonuncu elementlerin yerini  deyisib yaz
        Task70: test = "pythononon" stringinde ikinci o simvolunu a simvolu ile evez edin
        Task71: test = "pythononon" birinci ve sonuncu "o" simvollarini "a" simvolu ile evez edin
        Task72:test = "pythononon" stringinde "o" simvollarinin sayini cap eden python kodunu yazin
        Task73: test = "pythononon" stringinde ikinci "n" simvolunun indeksini cap eden python kodunu yazin
        Task74: test = "pythononon" stringinde sonuncu "n" simvolunun indeksini cap eden python kodunu yazin
        ''')

    def task_75_87(self):
        print('''Task75: #output: Steve loves learning of programming
                Task76: # output: Steve loves learning of science
                Task77: # output: Steve loves learning of engineering
                Task78: # output: Steve hates learning of programming
                Task79: # Output: Steve hates learning of science
                Task80: # Output: Steve hates learning of engineering
                Task81: # Output: Clare loves learning of programming
                Task82: # Output: Clare loves learning of science
                Task83: # Output: Clare loves learning of engineering
                Task84: # output: Clare hates learning of programming
                Task85:# Output: Clare hates learning of science
                Task86:# Output: Clare hates learning of engineering
                Task87: # Output: Steve and Clare love learning of programming

                ''')
        self.person = "Steve"
        self.person_ = "Clare"
        self.field1 = "programming"
        self.field2 = "science"
        self.field3 = "engineering"
        self.behave = "loves learning of"
        self.behave2 = "hates learning of"

        print(f"{self.person} {self.behave} {self.field1}")  ##output: Steve loves learning of programming
        print("{} {}{}".format(self.person, self.behave, self.field2))  # output: Steve loves learning of science
        print("{} {}{}".format(self.person, self.behave, self.field3))  # output: Steve loves learning of engineering
        print("{} {}{}".format(self.person, self.behave2, self.field1))  # output: Steve hates learning of programming
        print("{} {}{}".format(self.person, self.behave2, self.field2))  # Output: Steve hates learning of science
        print("{} {}{}".format(self.person, self.behave2, self.field3))  # Output: Steve hates learning of engineering
        print("{} {}{}".format(self.person_, self.behave, self.field1))  # Output: Clare loves learning of programming
        print("{} {}{}".format(self.person_, self.behave, self.field2))  # Output: Clare loves learning of science
        print("{} {}{}".format(self.person_, self.behave, self.field3))  # Output: Clare loves learning of engineering
        print("{} {}{}".format(self.person_, self.behave2, self.field1))  # output: Clare hates learning of programming
        print("{} {}{}".format(self.person_, self.behave2, self.field2))  # Output: Clare hates learning of science
        print("{} {}{}".format(self.person_, self.behave2, self.field3))  # Output: Clare hates learning of engineering
        print("{} and {} {}{}".format(self.person, self.person_, self.behave,
                                      self.field1))  # Output: Steve and Clare love learning of programming

    def task_88(self):
        print(
            '''level stringini bir deyisene menimsedib bir character buraxmaqla soldan saqa ve saqdan sola yazdirin''')
        self.a = 'level '
        print(self.a[::2])
        self.t = list(reversed(self.a[::2]))
        print(''.join(self.t))
        self.t = 'leeveel'
        print(self.t.replace('e', 'a', 2))

    def task_92_93(self):
        print('''Task92: level stringini ["l","e","v","e","l"] listi seklinde yazdirin''')
        self.test = 'level'
        print(list(self.test))

        self.test_ = 'level'
        self.test1 = self.test_.replace('e', '', 2)
        print(list(self.test1))

    def task_94_96(self):
        self.name = 'Timur'
        self.age = 30
        self.city = 'Baku'

        self.t = {'name': self.name, 'age': self.age, 'city': self.city}

        for i, j in self.t.items():
            print(i, j, end=' ')
            print(i, j, end=',')
            print(i, '\n', j, sep='')

    def tast_97(self):
        self.sample = "I am giving online classes"
        self.t = self.sample.split()
        print(self.t)

    def task_98(self):
        self.int_ = 42.3
        self.x = self.int_ // 10
        print(self.x)
        self.y = len(str(self.int_))
        print(self.y)
        print(pow(self.x, self.y))

    def task_99(self):
        self.int_ = 2.3
        self.x = self.int_ // 1
        print(self.x)
        self.y = len(str(self.int_))
        print(pow(self.x, self.y))

    def task_100(self):
        try:
            self.int_ = 23
            self.x = self.int_ // 10
            self.y = str(self.int_)[1]
            print(pow(self.x, self.y))
        except TypeError:
            print('string reqemle riyazi emeliyyata girmir')

    def task_101(self):
        self.int_ = 23
        self.x = self.int_ % 10
        self.y = str(self.int_)[1]
        print(pow(self.x, int(self.y)))

    def task_102(self):
        try:
            self.int_ = 23
            x = str(self.int_)[0]
            y = str(self.int_)[1]

            print(pow(x, int(y)))
        except TypeError:
            print('string reqemle riyazi emeliyyata girmir')

    def task_103(self):

        self.int_ = 23
        x = str(self.int_)[0]
        y = str(self.int_)[1]

        print(pow(int(x), int(y)))

    def task_106(self):

        self.a = 3.333
        print(int(self.a))
        print(round(self.a, 2))
        print(float(self.a))

    def task_107(self):
        self.str1 = " aBrbBBAaaabb"
        self.str1 = self.str1.strip()
        self.str1 = self.str1.swapcase()
        x = self.str1.find("B", 5, len(self.str1))
        print(self.str1[:x])

    def task_116_118(self):

        self.li = ['cola', 'pepsi', 'soft water', 'bizon']

        self.res = ','.join(self.li)  # vergul daxil
        self.res = ''.join(self.li)  # vergul daxil
        print(len(self.res))

        self.const_str = "Hello, World!"  # neticeni "Hello, JS" kimi yazdirin

        print(self.const_str.replace('World', 'JS'))

    def task_119(self):
        self.yaz = input('Soz daxil edin: ')
        print('daxil edilmis soz ', len(self.yaz), 'ibaretdir')

        self.asr = 'programming'  # Klaviaturadan daxil edilen 'programming' setrini 'program' kimi yazdirin

        print(self.asr[:7])

    def task_125(self):
        self.saat = int(input("Saat: "))
        self.deqiqe = int(input("Deqiqe: "))
        self.saniye = int(input("Saniye: "))
        print("sizin yazdiginiz vaxt {}:{}:{}".format(self.saat, self.deqiqe, self.saniye))

        self.ikinci_saat = int(input("Ikinci saat: "))
        self.ikinci_deqiqe = int(input("Ikinci deqiqe: "))
        self.ikinci_saniye = int(input("Ikinci saniye: "))
        print("sizin yazdiginiz vaxt {}:{}:{}".format(self.ikinci_saat, self.ikinci_deqiqe, self.ikinci_saniye))

        print("Netice", self.saniye - self.ikinci_saniye)


Ders_1()
