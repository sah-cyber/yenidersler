# lst = [True,"123",["pear","watermelon"]]
#
# print(type(lst))
#
# print(str(lst[0])[0])
#
# lst = [True,"123",["pear","watermelon"],123]
#
# #print(len(str(lst[0])))
#
# #print(lst[len(lst[3])])
#
#
# # print(lst[len(str(lst[3]-1))])
# print(type(lst[int(len(str(lst[3]))//1)]))

# items = ["gadget",["kiwi","pear","watermelon"],[["volo","audi"],["microphone",["Oxford","Harvard"],"math","manager"],"vehicle","airplane"]]
#
# print(items[2][1][0])

# items = ["gadget",["kiwi","pear","watermelon"],[["volvo","audi"],["microphone",["Oxford","Hardvard"],"math","manager"],"vehicle","airplane",["red","orange"],"grey"]]

# print(items[2][4][1].capitalize().replace('e','E'))

# items = ["gadget",["kiwi","pear","watermelon"],[["volo","audi"],["microphone",["Oxford","Harvard"],"math","manager"],"vehicle","airplane",["red","orange",["frontend","backend",["self-study","offline"]]],"grey"]]

# print(items[2][4][2][2][0].split('-'))

# items = [[["audi","lexus",["orange","purple"],"volvo"],[[True,False,"false"],"science","math",["engineering","doctor"]]],["pear","kiwi","apple"],[True,"microphone","scanner",[123],"127"]]


# it = items[2][3]
# it2 = items[2][4]
# for x in it:
#     print('son eded',int(x))
#     print('son eded',it2)
#     it2= int(it2)
#     print('son ededlerin cemi',(x%10)+(it2%10))

# print(items[2][3])
# print(items[2][4])

# str_ = items[0][1][0][1]
# str_ = str(str_)
# print(str_[0])
#
#
# lst = [[1,2],[3,4]]
# print(sum(lst,[]))

# gadgets = ['tablet','speaker','headphone','wearable','camera']

# gadgets.remove('camera')
# print(gadgets)
# mobil = 'mobile phone'  in gadgets
# print(mobil)
# gadget_1 = gadgets.copy()
# print(id(gadget_1))
# print(id(gadgets))
# if id(gadget_1) == id(gadgets):
#     print('Eynidir')
# else:
#     print("eyni deyil")
#
# # gadgets[gadgets.index('headphone')] = 'earbuds'
# # print(gadgets)
#
# gadgets.insert(2,'earbuds')
# # print(gadgets)

# gadgets.append(set('personal camputer','alma'))
# print(gadgets)
#
# my_tuple = ('personal camputer','musicplayer')
# gadgets.append(my_tuple)
# print(gadgets)

#my_list = ['personal camputer','musicplayer']
# gadgets.append(my_list)
# new_mylist = ['earphone','digital audio']
# #my_list.append(new_mylist)
# # #
# # # #print(gadgets)
# # #
# # # gadgets.append(my_list)
# # # print(gadgets)
# # my_tuple = ('personal camputer','musicplayer')
# # gadgets.append(my_tuple)
# gadgets.append(new_mylist)
# print(gadgets)
# print(gadgets[-1])
#
# del gadgets[-1]
# print(gadgets)
# #
# #
# gadgets = ['tablet','speaker','headphone','wearable']
# #print(sorted(gadgets))
# # gadgets.reverse()
# print(gadgets)
#
# gadgets.clear()
# print(gadgets)
#
# # gad_index = gadgets.index('speaker')
# #
# # del gadgets[gad_index]
# # print(gadgets)
# items = ["gadget",["kiwi","pear","watermelon"],[["volo","audi"],["microphone",["Oxford","Harvard"],"math","manager"],"vehicle","airplane",["red","orange",["frontend","backend",["self-study","offline"]]],"grey"]]
#print(items[2])
# print(items[2][5])
# colors = ["red","green","blue"]
# # del items[2][5]
# # print(items)
# #
# items[2].extend(colors)
# # #
# print(items)
# # items.append('grey')
# # print(items)
# # print(items[2][4][2][2][0])
# #
# # it = items[2][4][2][2][0]
# # it2 = ''.join(it)
# # print(it2[5:])
#
# items[2][0].insert(0,'toyata')
# print(items)
# items[2][4][2][0],items[2][4][2][1] = items[2][4][2][1],items[2][4][2][0]
# print(items)
#
# print(items[1][2])
#
# items[1][2]='weter-melon'
# print(items)

# print(items[2])
# print(items[2][1])
# print(items[2][1][1])
# it = items[2][1][1]
# items[2][1][1].append('CAmbridce')
# print(it)
# it.append('Cambridce')
# print(it)
# print(items[2][4][2])
# items[2][4][2].insert(0,'fullstack')
# str_ = str(items[2][4][2][0])
# str_=str_.upper()
# print(str_.upper())
# #print(items[2][4][2][0])
# # items[2][4][2].insert(0,str_)
# # print(items)
# # del items[2][4][2][1]
# items = ["gadget",["kiwi","pear","watermelon"],[["volo","audi"],["microphone",["Oxford","Harvard"],"math","manager"],"vehicle","airplane",["red","orange",["frontend","backend",["self-study","offline"]]],"grey"]]
# # print(items)
# # print(items[2][1])
# # items[2][1].insert(0,'microprocessor')
# # print(items)
# colors = ["red","green","blue"]
#
# print(colors[1])
# print(items[2])
# print(items[2][1])
# print(items[2][3])
# print(items[2][4])
# print(items[2][5])
#
# items[2].append(colors[1])
#
# #print(items)

# mylist = ['scaner','notepad','smartphone','mause']
# mytuple = ('HDD','SDD')
#
# mylist.insert(1,mytuple)
# print(mylist)

# lst = [10,25,4,12,3,8]
# lst = sorted(lst)
# print('53::',lst)

# num = [10,20,30,40,50]
# print(type(num))
# num[2:4]=[]
# print(num)
#
# x  = [1,2,3,4,5]
#
# print(x[1:4:2])
# y=x[1:4:2]
# print(y)

#
# i = j = [3]
# i+=j
# print(i)


# list1 = [1,2,4,3]
# list2 = [1,2,3,4]
#
# print(list1!=list2)

# l = [20, -5, 10, 100, 9, 1]
#
#
#
# l1 = [i for i in l if i > 0]
# print(l1)
# lst = [20, -5, 10, 100, 9, 1]



# t = l.index(min(l))
# b = l.index(max(l))
# print(t)
# print(b)
#
# l.insert(b,t)
# print(l)
# lst = [20, -5, 10, 100, 9, 1]
# min_index = lst.index(min(lst))
# print(min_index)
#
# max_index = lst.index(max(lst))
#
# print(max_index)
#
# lst[max_index],lst[min_index]=lst[min_index],lst[max_index]
#
# print(lst)


# a = input("Soz daxil edin ::")
# s = a.replace(' ','')
# print(s)
# print(len(s))


l = [[1,2,3],[4,5,6,7],[8,9,10,11,12]]


flat_list = [item for sublist in l for item in sublist if item % 2 != 0]




for i in flat_list:
    if i % 2 != 0:
        print(i**3)

cubes = [num ** 3 for num in flat_list if num % 2 != 0]

# Siyahını vergüllə ayıraraq çap etmək
print(", ".join(map(str, cubes)))





