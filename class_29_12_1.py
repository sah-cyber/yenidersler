

class YPerson:
    personal = {}

    def __init__(self,name,age,vezifesi):
        self.name = name
        self.age = age
        self.vezifesi = vezifesi


    def personal_yaz(self):
        self.personal[self.name]={'Yas':self.age,'Vezifesi':self.vezifesi}
        print(f"{self.name} adli sexs siyahiya yazildi")


    def personal_goruntule(self):
        print('Personal listesi')
        for k,v in self.personal.items():
            print(f"Personal adi:{k},Yasi:{v['Yas']},Vezifesi: {v['Vezifesi']}")


    @classmethod
    def personal_sayi(cls):
        print(f"Personal sayi {len(cls.personal)}")


ahmed = YPerson('Shahin',41,'Muhafize')
ahmed.personal_yaz()
# ahmed.personal_goruntule()
# ahmed.personal_sayi()
nubar = YPerson('Nubar',28,'Asbaz')
nubar.personal_yaz()
# nubar.personal_goruntule()
# nubar.personal_sayi()

mahmud = YPerson('Mahmud',22,'Kameraman')
mahmud.personal_yaz()
mahmud.personal_goruntule()


YPerson.personal_sayi()

