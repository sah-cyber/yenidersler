


class Listler:
    def __init__(self):
        self.task_1()
        self.task_13()
        self.task_17()
        self.task_19()
        self.task_21()
        self.task_23()
        self.task_29()
        self.task_35()
        self.task_36()
        self.task_37()
        self.task_38()
        self.task_40()
        self.task_42()
        self.task_44()
        self.task_52()
        self.task_65()
        self.task_66()



    def task_1(self):
        print("Tasklar: ")
        print('''lst = [True, "123", ["pear", "watermelon"]] verilmis deyisenin
        tipini yoxlayan python kodu yazin''')

        self.lst = [True, "123", ["pear", "watermelon"]]
        print('1::',type(self.lst))
        print('2::',str(self.lst[0])[0])

        try:

            self.lst2 = [True, "123", ["pear", "watermelon"], 123]

            print(len(self.lst2[0]))
        except TypeError:
            print("3:: Xeta INT uzunlugu olmur")

        print('4::',len(str(self.lst2[0])))

        try:
            print(self.lst2[len(str(self.lst2[0]))])
        except IndexError:
            print('5:: Xeta, Indexden kenardadir')

        print('6::',self.lst2[len(str(self.lst2[1]))])

        print('7::',self.lst2[len(self.lst2[2])])

        try:
            print('7::', self.lst2[len(self.lst2[2])])

        except IndexError:
            print('8:: Xeta,INT uzunlugu olmur')

        print('9::',self.lst2[len(str(self.lst2[3]-1))])

        print('10::',type(self.lst2[int(len(str(self.lst2[3]-1)))]))

        print('11::',type(self.lst2[int(len(str(self.lst2[3]-2)))]))
        print('12::',type(self.lst2[int(len(str(self.lst2[3]))//1)]))



    def task_13(self):
        self.items = ["gadget", ["kiwi", "pear", "watermelon"],
                 [["volo", "audi"], ["microphone", ["Oxford", "Harvard"], "math", "manager"], "vehicle", "airplane"]]

        print('13::',self.items[2][1][1][1])
        print('14::',self.items[2][1][1][0])
        print('15::',self.items[2][1][1][0].lower())
        print('16::', self.items[2][1][0])


    def task_17(self):
        self.items = ["gadget", ["kiwi", "pear", "watermelon"],
                 [["volvo", "audi"], ["microphone", ["Oxford", "Hardvard"], "math", "manager"], "vehicle", "airplane",
                  ["red", "orange"], "grey"]]

        print('17::',self.items[2][4][1])
        print('18::',self.items[2][4][1].capitalize().replace('e', 'E'))


    def task_19(self):
        self.items = ["gadget", ["kiwi", "pear", "watermelon"],
                 [["volo", "audi"], ["microphone", ["Oxford", "Harvard"], "math", "manager"], "vehicle", "airplane",
                  ["red", "orange", ["frontend", "backend", ["self-study", "offline"]]], "grey"]]

        print('19::',self.items[2][4][2][2][0].split('-'))

    def task_21(self):
        self.items = [[["audi", "lexus", ["orange", "purple"], "volvo"],
                  [[True, False, "false"], "science", "math", ["engineering", "doctor"]]], ["pear", "kiwi", "apple"],
                 [True, "microphone", "scanner", [123], "127"]]

        self.it = self.items[2][3]
        self.it2 = self.items[2][4]
        print('\t21::')
        for x in self.it:
            print('son eded', int(x))
            print('son eded', self.it2)
            it2 = int(self.it2)
            print('son ededlerin cemi', (x % 10) + (it2 % 10))

        str_ = self.items[0][1][0][1]
        str_ = str(str_)
        print('22::',str_[0])


    def task_23(self):
        self.lst = [[1, 2], [3, 4]]
        print('23::',sum(self.lst, []))

        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable', 'camera']

        self.gadgets.remove('camera')
        print('24::',self.gadgets)
        self.gadgets.remove('headphone')
        print('25::', self.gadgets)
        mobil = 'mobile phone' not in self.gadgets
        print('26::',mobil)
        mobil = 'mobile phone'  in self.gadgets
        print('27::', mobil)
        print('\t 28::')

        self.gadget_1 = self.gadgets.copy()
        print(id(self.gadget_1))
        print(id(self.gadgets))
        if id(self.gadget_1) == id(self.gadgets):
            print('Eynidir')
        else:
            print("eyni deyil")




    def task_29(self):

        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable', 'camera']
        self.gadgets[self.gadgets.index('headphone')] = 'earbuds'
        print('29::', self.gadgets)

        self.gadgets.insert(2, 'earbuds')
        print('30::',self.gadgets)
        self.gadgets.append('personal camputer')
        print('31::',self.gadgets)
        print('32::',"self.gadgets.append('personal camputer','camputer'-apend 1 soz elave ede bilir)")
        self.my_tuple = ('personal camputer','musicplayer')
        self.gadgets.append(self.my_tuple)
        print('33::',self.gadgets)
        self.my_list = ['personal camputer', 'musicplayer']
        self.gadgets.remove(self.my_tuple)
        self.gadgets.append(self.my_list)
        print('34::',self.gadgets)
        self.n_my_list = ['earphone','digital audio']



    def task_35(self):
        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable', 'camera']
        self.my_list = ['personal camputer', 'musicplayer']
        self.n_my_list = ['earphone', 'digital audio']
        self.my_list.append(self.n_my_list)
        self.gadgets.append(self.my_list)
        print('35::', self.gadgets)


    def task_36(self):
        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable', 'camera']
        self.my_list = ['personal camputer', 'musicplayer']
        self.n_my_list = ['earphone', 'digital audio']
        self.gadgets.extend(self.n_my_list)
        self.gadgets.append(self.my_list)
        print('36::', self.gadgets)

    def task_37(self):
        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable', 'camera']
        self.my_tuple = ('personal camputer', 'musicplayer')
        self.n_my_list = ['earphone', 'digital audio']
        self.gadgets.append(self.my_tuple)
        self.gadgets.append(self.n_my_list)

        print('37::', self.gadgets)


    def task_38(self):
        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable']
        self.gad_index = self.gadgets.index('speaker')
        del self.gadgets[self.gad_index]
        print('38::',self.gadgets)
        self.gadgets.append('speaker')
        print('39::',sorted(self.gadgets))




    def task_40(self):
        self.gadgets = ['tablet', 'speaker', 'headphone', 'wearable']
        print('\t 40::')
        print(self.gadgets)
        self.gadgets.remove('wearable')
        self.gadgets.insert(0, 'wearable')
        print(self.gadgets)
        self.gadgets.clear()
        print('41::',self.gadgets)


    def task_42(self):
        self.items = ["gadget", ["kiwi", "pear", "watermelon"],
                 [["volo", "audi"], ["microphone", ["Oxford", "Harvard"], "math", "manager"], "vehicle", "airplane",
                  ["red", "orange", ["frontend", "backend", ["self-study", "offline"]]], "grey"]]

        it = self.items[2][4][2][2][0]
        it2 = ''.join(it)
        print('42::',it2[5:])

        #43 sual
        print(self.items[2][5])
        self.colors = ["red", "green", "blue"]
        del self.items[2][5]
        print(self.items)
        self.items.extend(self.colors)
        print(self.items)
        self.items.append('grey')
        print('43::',self.items)

    def task_44(self):
        self.items = ["gadget", ["kiwi", "pear", "watermelon"],
                      [["volo", "audi"], ["microphone", ["Oxford", "Harvard"], "math", "manager"], "vehicle",
                       "airplane",
                       ["red", "orange", ["frontend", "backend", ["self-study", "offline"]]], "grey"]]

        self.colors = ["red", "green", "blue"]

        self.items[2].extend(self.colors)
        print('44::',self.items)

        self.items[2][0].insert(0,'toyota')
        print('45::', self.items)

        self.items[2][4][2][0], self.items[2][4][2][1] = self.items[2][4][2][1], self.items[2][4][2][0]
        print('46::',self.items)
        self.items[1][2] = 'weter-melon'
        print('47::',self.items)
        self.items[2][1][1].append('Cambridce')
        print('48::',self.items)
        #49

        self.items[2][4][2].insert(0, 'fullstack')
        self.str_ = str(self.items[2][4][2][0]).upper()
        #self.str_ = self.str_.upper()
        self.items[2][4][2].insert(0, self.str_)
        del self.items[2][4][2][1]

        print('49::',self.items)

        self.items[2][1].insert(0, 'microprocessor')
        print('50::',self.items)
        del self.items[2][6:9]
        self.items[2].append(self.colors[1])
        print('51::',self.items)

    def task_52(self):

        self.mylist = ['scaner', 'notepad', 'smartphone', 'mause']
        self.mytuple = ('HDD', 'SDD')

        self.mylist.insert(1, self.mytuple)
        print('52::',self.mylist)

        lst = [10,25,4,12,3,8]
        sorted(lst)
        print('\t53::\n',lst,sep='')
        lst = sorted(lst)
        print(lst)
        print()

        lst1 = [10,25,4]
        print('54::',sorted(lst1))

        num = [10, 20, 30, 40, 50]
        #print(type(num))
        num[2:4] = []
        print('55::',num)

        x = [1, 2, 3]
        y = x * 2
        y[0] = 0
        print('56::',y)
        y[1]=5
        print('57::',y)

        x = [1, 2, 3, 4, 5]

        #print(x[1:4:2])
        y = x[1:4:2]
        print('58::',y)

        i = j = [3]
        i += j
        print('59::',i, j)

        list1 = [1, 2, 4, 3]
        list2 = [1, 2, 3, 4]
        print('60::',list1 != list2)

        l = [20, -5, 10, 100, 9, 1]

        l1 = [i for i in l if i > 0]
        print('61::',l1)
        l2 = [i for i in l if i < 0]
        print('62::', l2)
        print('63::',l[0] + l[-1])

        lst = [20, -5, 10, 100, 9, 1]

        print('\t64::\n',lst,sep='')


        min_index = lst.index(min(lst))
        #print(min_index)

        max_index = lst.index(max(lst))
        #print(max_index)
        lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

        print(lst)


    def task_65(self):
        a = input("Soz daxil edin: ")
        s = a.replace(' ', '')
        print(s)
        print('65:: {} sozunde {} herf var'.format(a,len(s)))


    def task_66(self):
        l = [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]

        flat_list = [item for sublist in l for item in sublist if item % 2 != 0]
        print(flat_list)
        kubu = [num ** 3 for num in flat_list if num % 2 != 0]
        print('66:: ededin kubu',kubu)

        birlikde = [i for k in l for i in k]
        print('67:: ',birlikde)


Listler()
