

class Listler:
    def __init__(self):
        self.task()
        self.task_1()
        self.task_2()
        self.task_3()
        self.task_4()
        self.task_5()
        self.task_6()
        self.task_7()
        self.task_8()



    def task(self):
        import random

        mylist = []
        mylist_1 = []
        while True:
            eded_1 = random.randint(1, 20)
            eded_2 = random.randint(1, 20)
            mylist.append(eded_1)
            mylist_1.append(eded_2)
            if eded_1 == eded_2:
                break

        print('birinci list', mylist)
        print('ikinci list', mylist_1)

        eded_1_set = set()
        eded_2_set = set()

        for i in mylist:
            eded_1_set.add(i)
            for j in mylist_1:
                eded_2_set.add(j)
        print('eded1 birin seti', eded_1_set)
        print('eded 2 nin seti', eded_2_set)

        intersektion = eded_1_set & (eded_2_set)
        print('eded1 aid')
        print(intersektion)

        diferense_set_1 = eded_1_set - eded_1_set
        print(diferense_set_1)

        simmetrik_diference_1 = eded_2_set ^ eded_1_set
        print(simmetrik_diference_1)

        union_1 = eded_1_set.union(eded_2_set)
        print(union_1)

        print('eded2 aid')
        intersektion_2 = eded_2_set & (eded_1_set)
        print(intersektion_2)

        diferense_set = eded_2_set - eded_1_set
        print(diferense_set)

        simmetrik_diference = eded_1_set ^ eded_2_set
        print(simmetrik_diference)

        union = eded_2_set.union(eded_1_set)
        print(union)


    def task_1(self):
        tuple1 = (1, 2, 3)
        tuple2 = ('a', 'b', 'c')
        tuple3 = tuple1 + tuple2

        print('\t1::\nTuple 1: ', tuple1)
        print('Tuple 2: ', tuple2)
        print('Combined Turle: ', tuple3)

        fruits = ('apple', 'banana', 'orange')

        print('2::',fruits[1])

        number_list = [1, 2, 3, 4, 5]

        number_tuple = tuple(number_list)
        print('3::\n', number_list)
        print(number_tuple)

        coordinates = (3, 4)

        print("4::\nx: {}\ny: {}".format(coordinates[0], coordinates[1]))
        colors = {'red', 'green', 'blue', 'yellow', 'purple'}
        print('5::')
        for i in colors:
            print(i)
        print('6::')

        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}

        union_t = set1.union(set2)
        intersection_t = set1.intersection(set2)
        difference_t = set1.difference(set2)
        difference_t2 = set2.difference(set1)
        print(union_t)
        print(intersection_t)
        print(difference_t)
        print(difference_t2)

        #colors = {'red', 'green', 'blue', 'yellow', 'purple'}

        colors.add('blak')
        yenireng = ['sari', 'yasil', 'qirmii']

        print('7::\n',colors,sep='')
        colors.update(yenireng)
        print(colors)

        del colors
        try:
            print(colors)
        except NameError:
            print('11:: Silindi')

        animal = {'lion', 'elephant', 'giraffe', 'tiger', 'zebra', 'cat'}
        print('12::',animal)

        string_ = ['father', 'mother', 'sister', 'brother']

        string_ = set(string_)
        print('13::',string_)

        animal.remove('cat')
        print('14::',animal)


    def task_2(self):
        person = {
            'name': 'Shahin',
            'age': 41,
            'city': 'Baku'
        }
        #
        # for i in person:
        #     print(person[i])
        print('15::')
        for k, v in person.items():
            print(k, v)

        print('16::', person['name'])

        person['occupation'] = 'engineer '
        print('17::', person)

        person['new age'] = person.pop('age')
        print('18::', person)

        del person['city']
        print('19::', person)
        print('20::')
        for i in person.keys():
            print(i)
        print('21::')
        for i in person.values():
            print(i)


    def task_3(self):
        print('22::')
        eded_kvadrat = {i: i ** 2 for i in range(1, 6)}
        print(eded_kvadrat)

        eded_dict = {}
        for s in range(1, 6):
            eded_dict[s] = s ** 2

        print(eded_dict)


        ad = input("MUellif adini daxil edin: ")

        kitablar = input("Kitablarini daxil edin ")

        kitab = kitablar.split(" ")

        dict_ = {ad: kitab}
        print('23::',dict_)

        name = input("Enter your name: ")
        last_name = input("Enter your last name: ")

        person = {'name': name, 'last_name': last_name}
        print('24::')
        print(person)
        for k, v in person.items():
            print(k, v)

        for k in person:
            print(person[k])

        marks = {"Gunay": 223,
                 "Mahir": 254,
                 "Nermine": 270,
                 "Resid": 260,
                 "Roya": 231}

        t = max(marks.values())
        print('25::')

        for k, v in marks.items():
            if v == t:
                print(k, v)

        #
        telebe = max(marks, key=marks.get)
        print(f'{telebe}, {marks.get(telebe)}')
        print(f'{telebe}, {marks[telebe]}')

        print('26::')
        t = min(marks.values())

        for k, v in marks.items():
            if v == t:
                print('min', k, v)

        min_bal = min(marks, key=marks.get)

        print(f'{min_bal}, {marks.get(min_bal)}')

        boyuk_bal = max(marks, key=marks.get)
        kicik_bal = min(marks, key=marks.get)

        print(f"yuksek bal yigan {boyuk_bal}-{marks.get(boyuk_bal)} bal ,kicik bal yigan {kicik_bal}-{marks.get(kicik_bal)} bal")


    def task_4(self):
        anbar = {}

        alinan_malin_sayi = int(input("Alinan malin sayini daxil edin: "))

        for i in range(alinan_malin_sayi):
            malin_adi = input('Malin adini qeyd edin: ')
            malin_deyeri = int(input('Malin deyeri qeyd edin: '))

            anbar[malin_adi] = malin_deyeri
        print(anbar)
        total = sum(anbar.values())
        casbak = total * 0.03
        print('\nAlinan mallar ve qiyetleri:')
        for k, v in anbar.items():
            print(f'{k}: {v}')
        print(f'xercler {total} manat')
        print(f'casbak {casbak} manat')

    def task_5(self):
        telebeler = {"Ali": {'yas': 17, 'field': 'Computer Science', 'marks': [4, 5, 3]},
                     "Elqar": {"yas": 17, "field": 'Computer Engineering', 'marks': [4, 5, 6]}}
        bos = []
        for k, v in telebeler.items():
            if k == 'Ali':
                print(v['marks'])
                for i in v['marks']:
                    t = int(i) * 2
                    s = str(t)
                    bos.append(s)
                print(bos)

    def task_6(self):
        import random
        students = {
            "Oman": {
                "age": 20,
                "major": "Computer Science",
                "marks": [4, 5, 8],
                "scores": [85, 90, 92],
            },
            "Lawrence": {
                "age": 19,
                "major": "Information technology",
                "marks": [6, 4, 7],
                "scores": [75, 80, 90],
            },
            "Keen": {
                "age": 18,
                "major": "Cyber security",
                "marks": [8, 7, 9],
                "scores": [77, 89, 93],
            },
            "Samar": {
                "age": 21,
                "major": "Information Security",
                "marks": [6, 8, 7],
                "scores": [75, 80, 90],
            },
            "James": {
                "age": 22,
                "major": "Computer Science",
                "marks": [6, 8],
                "scores": [65, 69, 74],
            },
            "Marvin": {
                "age": 18,
                "major": "Computer Engineering",
                "marks": [5, 7, 9],
                "scores": [95, 79],
            },
        }

        cap = students['Oman']['age']
        print('30::', cap)

        cap1 = students['Oman']['major']
        print('31::', cap1)
        cap2 = students['Oman']['marks']
        print('32::', cap2)

        cap3 = students['Oman']['marks']
        ortalama = sum(cap3) / len(cap2) if cap3 else 0
        print('33::', cap3)
        print(f'ortalm qiymet {ortalama:.2f}')

        cap4 = students['Oman']['scores']
        print('34::', cap4)

        cap5 = students['Oman']['scores']

        ortalamascore = sum(cap5) / len(cap4) if cap5 else 0
        print('35::', ortalamascore)
        print('36-37::')
        if ortalamascore < 70:
            print("Buraxilmir")
        elif ortalamascore < 50:
            print("Teqaudu kesilsin")
        else:
            print('Buraxilir')

        print('38::')

        for k, v in students.items():
            for m in v['marks']:
                if m > 5:
                    print(f'{k}:{m}')

        print('39::')
        for k, v in students.items():
            if v['age'] > 20:
                print(f'{k}')

        print('40::')
        ran = random.randint(5, 10)
        print(ran)
        for k, v in students.items():
            if len(v['marks']) < 3:
                v['marks'].append(ran)
                print(k, v['marks'])

        print('41::')
        # score = random.randint(60,99)

        for k, v in students.items():
            if len(v['scores']) < 3:
                print(f'{k}{v['scores']}')
                v['scores'].append(random.randint(60, 100))
                print(k, v['scores'])

        print('42::')
        for k, v in students.items():
            if v['scores'] == sorted(v['scores']):
                print(f'{k}{v["scores"]}')


    def task_7(self):
        import random
        mylist = []
        mylist1 = []
        while True:

            eded_bir = random.randint(1, 21)
            eded_bir2 = random.randint(1, 21)
            mylist.append(eded_bir)
            mylist1.append(eded_bir2)

            if len(mylist) == 20:
                break

        ilkset = set(mylist)
        sonset = set(mylist1)

        print(mylist)
        print(mylist1)
        print('********')
        print(ilkset)
        print(sonset)

        union = ilkset | sonset
        print('Union: ', union)

        intersection = ilkset & sonset
        print('Intersection: ', intersection)

        difference = ilkset - sonset
        print('Difference: ', difference)

        symmetric_difference = ilkset ^ sonset
        print('Symmetric Difference: ', symmetric_difference)


    def task_8(self):
        print('44::')
        import random
        mylist = []
        mylist1 = []
        while True:

            eded_bir = random.randint(1, 21)

            if eded_bir % 2 == 0:
                mylist.append(eded_bir)

            else:
                mylist1.append(eded_bir)
            if len(mylist) == 20:
                break

        print(mylist)
        print(mylist1)

        myset = set(mylist + mylist1)
        print(myset)

        mylist.extend(mylist1)
        print(mylist)


Listler()