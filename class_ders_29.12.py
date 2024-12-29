

class Personal:
    personal = []
    yas =[]

    def __init__(self, name):
        self.name = name


        self.personal_kabiliyyet =[]
        self.personal_yaz()



    def personal_yaz(self):
        self.personal.append(self.name)
        print(f"{self.name} adli sexs personal siyahisina yazildi")



    @classmethod
    def personal_sayi(cls):
        print(len(cls.personal))

    def personal_goruntule(self):
        print('Personal listesi')
        for kisi in self.personal:
            print(kisi)

    def personal_kabiliyet_yaz(self,kabiliyyet):
        self.personal_kabiliyyet.append(kabiliyyet)

    def kabiliyyet_goruntule(self):
        print(f"{self.name} adli personalin kabiliyetleri")
        for kabil in self.personal_kabiliyyet:
            print(kabil)

    def yas_ekle(self,yasi):
        self.yas.append(yasi)
        print(f"{self.yas} siyahiya salindi")

    def yas_goster(self):
        for y in self.yas:
            print(y)


ahmed = Personal('Ahmed')

ahmed.personal_sayi()
ahmed.personal_kabiliyet_yaz('muhavuize')
ahmed.kabiliyyet_goruntule()
ahmed.yas_ekle(28)
ahmed.yas_goster()

mehmed = Personal('Mehmed')
mehmed.yas_ekle(30)
mehmed.yas_goster()
mehmed.personal_goruntule()
mehmed.personal_sayi()
mehmed.personal_kabiliyet_yaz('axran')
mehmed.kabiliyyet_goruntule()



