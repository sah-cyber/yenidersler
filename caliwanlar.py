


# class Calisan:
#     __personal = []
#
#
#     def __init__(self, isim):
#         self.isim = isim
#         self.kabiliyyet = []
#         self.__personal_yaz()
#
#
#     @classmethod
#     def personal_sayi(cls):
#         print(len(cls.__personal))
#
#
#     def __personal_yaz(self):
#         self.__personal.append(self.isim)
#         print(f"{self.isim} adli sexs personal siyahisina elave olundu")
#
#
#     def kabiliyyet_yaz(self,kabiliyyet):
#         self.kabiliyyet.append(kabiliyyet)
#         print(f"{self.isim} adli sexsin {kabiliyyet} elave olundu")
#
#
#     def kabiliyyer_goster(self):
#         print(f"{self.isim} adli sexsin kabiliyyetleri")
#         for kabiliiyet in self.kabiliyyet:
#             print(kabiliiyet)
#
#
#
# ahmed = Calisan('Ahmed')
# ahmed.kabiliyyet_yaz('muhavize')
# ahmed.personal_sayi()
# ahmed.kabiliyyer_goster()
# #ahmed.__personal_yaz()
# ahmed._Calisan__personal_yaz()



class Calisan:
    _personal = []


    def __init__(self, isim):
        self._isim = isim
        self.kabiliyyet = []
        self.personal_yaz()


    @classmethod
    def personal_sayi(cls):
        print(f"Siyahida personal sayi {len(cls._personal)} neferdir")


    def personal_yaz(self):
        self._personal.append(self._isim)
        print(f"{self._isim} adli sexs personal siyahisina elave olundu")


    def kabiliyyet_yaz(self,kabiliyyet):
        self.kabiliyyet.append(kabiliyyet)
        print(f"{self._isim} adli sexsin {kabiliyyet} elave olundu")


    def kabiliyyer_goster(self):
        print(f"{self._isim} adli sexsin kabiliyyetleri")
        for kabiliiyet in self.kabiliyyet:
            print(kabiliiyet)


    @classmethod
    def personal_goruntule(cls):
        say = 0
        print('Personal listesi')
        for personal in cls._personal:
            say += 1
            print(f"{say}.{personal}")

    @property
    def isim__a(self):
        return self._isim


    @isim__a.setter
    def isima(self,yeni_isim):
        kisi = self._personal.index(self.isim__a)
        self._personal[kisi] = yeni_isim
        print('Yeni Isim:',yeni_isim)



ahmed = Calisan('Ahmed')
ahmed.kabiliyyet_yaz('muhavize')
ahmed.kabiliyyer_goster()
print('*'*20)
mehmed = Calisan('Mehmet')
mehmed.kabiliyyet_yaz('elektrik')
mehmed.kabiliyyet_yaz('mantyor')
mehmed.kabiliyyer_goster()
print('*'*20)
Calisan.personal_sayi()
# ahmed.isim = 'Sahin'
# print(ahmed.isim)
ahmed.personal_goruntule()
#kisi = Calisan.personal.index('Ahmed')
#Calisan.personal[kisi]='Sahin'
# Calisan.personal_goruntule()
#
# mehmed.isim_deyisdir('EMre')
# Calisan.personal_goruntule()

mehmed.isima = 'XXXXX'

Calisan.personal_goruntule()