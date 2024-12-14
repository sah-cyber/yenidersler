
#3 öğeden oluşan bir liste oluşturun ve liste kavramayı kullanarak her öğenin üçüncü gücünü hesaplayın.
def kub():
    print('1::')
    list = [5,8,9]

    mylist = [*map(lambda x:x**3,list)]
    print(mylist)
kub()

def soz_duzlt():
    print('2::')
    words = 'Data Science Academy offers the best data analysis courses in Brazil'.split()
    result = map(lambda w: [w.upper(),w.lower(),len(w)],words)
    print(*result,sep='\n')

soz_duzlt()

def tek_cut_number():
    print('3::')
    matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
    transport = [[t[i] for t in matrix] for i in range(2)]
    print(transport)

    transp_cut = filter(lambda f: f%2==0,[i for j in matrix for i in j])
    print(list(transp_cut))
    transp_tek = filter(lambda x: x%2 !=0,[k for t in matrix for k in t])
    print(list(transp_tek))
tek_cut_number()

print('4::')
listOfNumbers = [0, 1, 2, 3, 4]
from functools import reduce
def kvadrat(x):
    return x**2

def kub(x):
    return x**3

funck = [kvadrat,kub]

for i in listOfNumbers:
    result = map(lambda x: x(i),funck)
    print(list(result))

res = reduce(lambda x,f: f(x),funck,listOfNumbers[0])


print(res)


def yukselis():
    print('5::')
    listA = [2, 3, 4]
    listB = [10, 11, 12]
    result = map(pow, listA, listB)
    print(list(result))
yukselis()

def menfi_deyer():
    print('6::')
    range(-5,5)
    result = filter(lambda x: x<0,range(-5,5))
    print(list(result))
menfi_deyer()


def ortaq():
    print('7::')
    a = [1, 2, 3, 5, 7, 9]
    b = [2, 3, 5, 6, 7, 8]

    result= [*filter(lambda x: x in a,b)]
    print(result)
ortaq()


def zaman():
    print('8::')
    import datetime
    print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
    import time

    zaman_ = time.strftime('%d/%m/%Y %H:%M')
    print(zaman_)
    indiki = datetime.date.today()
    print(indiki.strftime("%d/%m/%Y %H:%M"))

    yeni_z = datetime.datetime.now()
    print(yeni_z.strftime('%d/%m/%Y %H:%M'))


zaman()

print('9::')
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 4, 'd': 5}
def sozluk(d1,d2):


    dict3={}

    for d1key, d2val in zip(d1,d2.values()):
        dict3[d1key] = d2val
    return dict3

dict_ = sozluk(dict1,dict2)
print(dict_)

def indexi_tap():
    print('10::')

    lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    print(*enumerate(lista))

    for i,j in enumerate(lista):
       if i >5:
           print(j)

    result = filter(lambda x:x[0]>5, enumerate(lista))
    print(list(result))

    result = [*filter(lambda x:x[0]>5, enumerate(lista))]
    print(result)

    res = ' '.join([f"{index}, {value}" for index, value in result])
    print(res)

indexi_tap()

print('11::')
nums = (1, 2, 3, 4, 5, 6, 7)

def nums_topla(number):

    result = map(lambda x: x+x+x,number)

    return result

print(list(nums_topla(nums)))

print('12::')

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]


def cemleri(a, b, c):

    result = map(lambda x,y,z: x+y+z, a, b, c)
    return list(result)
print(cemleri(nums1, nums2, nums3))

print('13::')
color = ['Red', 'Blue', 'Black', 'White', 'Pink']
from functools import reduce

def renf(reng):
    # result= list(map(list,reng))
    # return result
    res = reduce(lambda a,x: a+[list(x)],reng,[])
    return res
print(renf(color))