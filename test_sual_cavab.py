import sys


class SualCavabOyunu:
    def __init__(self):
        self.dogru_cavab = 0
        self.sef_cavab = 0
        self.cavab_bend = ['A', 'B', 'C']
        self.start()



    def qrup_1(self):
        print('*' * 50)
        print('1-ci qrup üzrə Fenler')
        print("""
        1.Kimya
        2.Riyaziyyat
        3.Fizika
        4.Xarici dil
        5.İnformatika
        6.Azərbaycan dili\n""")

        print('*' * 50)
        self.kimya()
        self.riaziyyat()
        self.fizika()
        self.azerbaycan()
        self.informatika()
        self.xarici_diller()

    def qrup_2(self):
        print('*' * 50)
        print('2-ci qrup üzrə Fenler')
        print("""
        1.Coğrafiya
        2.Riyaziyyat
        3.Tarix
        4.Xarici dil
        5.Azərbaycan dili\n""")
        print('*' * 50)
        self.cografiya()
        self.riaziyyat()
        self.tarix()
        self.azerbaycan()
        self.xarici_diller()

    def qrup_3(self):
        print('*' * 50)
        print('3-cü qrup üzrə Fenler')
        print("""
        1.Ədəbiyyat
        2.Riyaziyyat
        3.Tarix
        4.İngilis dili,
        5.Azərbaycan dili\n""")
        print('*' * 50)
        self.edebiyyat()
        self.riaziyyat()
        self.tarix()
        self.azerbaycan()
        self.xarici_diller()

    def qrup_4(self):
        print('*' * 50)
        print('4-cü qrup üzrə Fenler')
        print("""
        1.Kimya
        2.Riyaziyyat
        3.Fizika
        4.İngilis dili,
        5.Azərbaycan dili
        6.Biologiya\n""")
        print('*' * 50)
        self.kimya()
        self.riaziyyat()
        self.fizika()
        self.azerbaycan()
        self.bialogiya()
        self.xarici_diller()

    def qrup_5(self):
        print('*' * 50)
        print('5-ci qrup üzrə Fenler')
        print("""
        1.Azərbaycan dili
        2.Riyaziyyat
        3.Xarici dili\n""")
        print('*' * 50)
        self.azerbaycan()
        self.riaziyyat()
        self.xarici_diller()

    def xarici_diller(self):
        print("Orta Mektebde Hansi Xarici dil tedris olunub")
        print("""Keçirilən Xarici dili qeyd edin
        1.Alman
        2.Fransız
        3.Rus
        4.İngilis 
        Seçiminizi fenn üzre reqemle qeyd edin məs: 1 düyməsi Alman. 2 düyməsi Fransız və.s""")

        while True:
            self.dil_secimi = input('Dil seçiminın nömrəsi: ')

            if self.dil_secimi.isdigit() and self.dil_secimi != "":
                if 1 <= int(self.dil_secimi) <= 4:
                    if self.dil_secimi == '1':
                        self.xarici_alman()
                        break

                    elif self.dil_secimi == '2':
                        self.xarici_fransiz()
                        break
                    elif self.dil_secimi == '3':
                        self.xarici_rus()
                        break
                    elif self.dil_secimi == '4':
                        self.xarici_ingilis()
                        break

                else:
                    print(f"{self.dil_secimi} düzgün seçim deyil. Seçiminiz 1-dən 4-ə qədər olmalıdır.")
            else:
                print(f"{self.dil_secimi} düzgün seçim deyil. Seçiminizi düzgün edin.")






    def control(self,fenn):
        for k, v in fenn.items():
            print(f"Sual: {k} : {v['sual']}")
            print('Cavablar')
            for cavab in v['cavablar']:
                print(cavab)

            self.cavab_ver = input('Hansi dogru bendir: ').upper()
            while self.cavab_ver not in self.cavab_bend:
                print("Seçiminizi düzgün edin. Yalnız A, B və ya C variantlarını seçə bilərsiniz.")
                self.cavab_ver = input("Hansını doğru bilirsiniz? (A, B, C): ").upper()

            if self.cavab_ver == v['dogru_cavab'][0]:
                print("Doğru cavab! 😊 Cavab:{}".format(v['dogru_cavab']))
                self.dogru_cavab += 1

            else:
                print(f"Sehv tapdiniz 😞. Dogru cavab: {v['dogru_cavab']}")
                self.sef_cavab += 1

            print('*' * 60)
        print(f"Doğru cavabların sayı: {self.dogru_cavab}")
        print(f"Səhv cavabların sayı: {self.sef_cavab}")
        self.kecid()

    def kecid(self):
        try:
            self.kecid_bal = (self.dogru_cavab * 5) - (self.sef_cavab * 2)
            print('Sizin keçid balınız', self.kecid_bal)
            if self.kecid_bal >= 90:
                qiymet = 'A'
            elif self.kecid_bal >= 80:
                qiymet = 'B'
            elif self.kecid_bal >= 70:
                qiymet = 'C'
            elif self.kecid_bal >= 60:
                qiymet = 'D'
            else:
                qiymet = 'F'  # Keçmədikdə 'F' verilir

            print(f"Ümumi balınız: {self.kecid_bal} bal - Qiymət: {qiymet}")
        except (ZeroDivisionError, OverflowError):
            print('Sizin səhfiniz yoxdur')

    def xarici_rus(self):
        print('#' * 50)
        print('--------------RUS---------------')

        self.rus_dict_questions = {
            1: {
                "sual": "Столица России?",
                "cavablar": ["A) Москва", "B) Санкт-Петербург", "C) Казань"],
                "dogru_cavab": "A) Москва"
            },
            2: {
                "sual": "Какое слово является глаголом?",
                "cavablar": ["A) Бегать", "B) Быстро", "C) Умный"],
                "dogru_cavab": "A) Бегать"
            },
            3: {
                "sual": "Какой день недели идет после понедельника?",
                "cavablar": ["A) Вторник", "B) Среда", "C) Четверг"],
                "dogru_cavab": "A) Вторник"
            }

        }
        self.control(self.rus_dict_questions)
        self.menu()

    def xarici_fransiz(self):
        print('#' * 50)
        print('--------------FRANSIZ---------------')

        self.fransiz_dict_questions = {
            1: {
                "sual": "Quelle est la capitale de la France ?",
                "cavablar": ["A) Paris", "B) Marseille", "C) Lyon"],
                "dogru_cavab": "A) Paris"
            },
            2: {
                "sual": "Quel est le plus grand océan du monde ?",
                "cavablar": ["A) Océan Atlantique", "B) Océan Pacifique", "C) Océan Indien"],
                "dogru_cavab": "B) Océan Pacifique"
            },
            3: {
                "sual": "Combien de mois dans une année ?",
                "cavablar": ["A) 10", "B) 12", "C) 14"],
                "dogru_cavab": "B) 12"
            }

        }
        self.control(self.fransiz_dict_questions)
        self.menu()

    def xarici_alman(self):
        print('#' * 50)
        print('--------------ALMAN---------------')
        self.alman_dict_questions = {
            1: {
                "sual": "Was ist die Hauptstadt von Deutschland?",
                "cavablar": ["A) Berlin", "B) München", "C) Frankfurt"],
                "dogru_cavab": "A) Berlin"
            },
            2: {
                "sual": "Welches ist der längste Fluss in Deutschland?",
                "cavablar": ["A) Rhein", "B) Elbe", "C) Donau"],
                "dogru_cavab": "A) Rhein"
            },
            3: {
                "sual": "Wie viele Bundesländer gibt es in Deutschland?",
                "cavablar": ["A) 12", "B) 16", "C) 18"],
                "dogru_cavab": "B) 16"
            }

        }
        self.control(self.alman_dict_questions)
        self.menu()

    def xarici_ingilis(self):
        print('#' * 50)
        print('--------------İNGİLİS---------------')

        self.english_dict_questions_azerbaijani = {
            1: {
                "sual": "İngiltərənin paytaxtı hansıdır?",
                "cavablar": ["A) London", "B) Paris", "C) Berlin"],
                "dogru_cavab": "A) London"
            },
            2: {
                "sual": "'Foot' sözünün çoxluq forması nədir?",
                "cavablar": ["A) Foots", "B) Feets", "C) Feet"],
                "dogru_cavab": "C) Feet"
            },
            3: {
                "sual": "Aşağıdakilerden hansıdır fel?",
                "cavablar": ["A) Run", "B) Happiness", "C) Quickly"],
                "dogru_cavab": "A) Run"
            }

        }

        self.control(self.english_dict_questions_azerbaijani)
        self.menu()



    def kimya(self):
        print('#' * 50)
        print('--------------KİMYA---------------')
        self.kimya_suallari = {
            1: {
                "sual": "Kimyada atomların ən kiçik vahidi hansı maddəyə aiddir?",
                "cavablar": ["A) Atom", "B) Molekul", "C) Ion"],
                "dogru_cavab": "A) Atom"
            },
            2: {
                "sual": "Hidrogenin kimyəvi simvolu hansıdır?",
                "cavablar": ["A) H", "B) He", "C) O"],
                "dogru_cavab": "A) H"
            },
            3: {
                "sual": "Su molekulunun (H2O) tərkibində neçə oksigen atomu vardır?",
                "cavablar": ["A) 1", "B) 2", "C) 3"],
                "dogru_cavab": "A) 1"
            }

        }

        self.control(self.kimya_suallari)

    def riaziyyat(self):
        print('#' * 50)
        print('--------------RİAZİYYAT---------------')
        self.riyaziyyat_suallari = {
            1: {
                "sual": "Bir üçbucağın iç bucaqlarının cəmi nə qədərdir?",
                "cavablar": ["A) 180°", "B) 360°", "C) 90°"],
                "dogru_cavab": "A) 180°"
            },
            2: {
                "sual": "Bir ədədi 7 ilə böləndə qalan 3 qalırsa, həmin ədədin böləni nədir?",
                "cavablar": ["A) 7", "B) 3", "C) 6"],
                "dogru_cavab": "A) 7"
            },
            3: {
                "sual": "Bir düzbucaqlı üçbucağın hipotenuzasının uzunluğu 10 sm, bir ayağının uzunluğu isə 6 sm-dir. İkinci ayağının uzunluğunu tapın.",
                "cavablar": ["A) 8 sm", "B) 7 sm", "C) 9 sm"],
                "dogru_cavab": "B) 8 sm"
            }

        }

        self.control(self.riyaziyyat_suallari)

    def fizika(self):
        print('#' * 50)
        print('--------------FİZİKA---------------')
        self.fizika_suallari = {
            1: {
                "sual": "Hərəkət nədir?",
                "cavablar": ["A) Cismin zamanla yer dəyişməsi", "B) Cismin sürətinin dəyişməsi",
                             "C) Cismin kütləsinin dəyişməsi"],
                "dogru_cavab": "A) Cismin zamanla yer dəyişməsi"
            },
            2: {
                "sual": "Newton-un birinci qanunu nəyi izah edir?",
                "cavablar": ["A) Qüvvə olmadan hərəkət edən cism sabit sürətini saxlayır",
                             "B) Qüvvə hərəkət edən cismi dayandırır", "C) Cismin hərəkətini yalnız sürət təsir edir"],
                "dogru_cavab": "A) Qüvvə olmadan hərəkət edən cism sabit sürətini saxlayır"
            },
            3: {
                "sual": "Kinetik enerji necə hesablanır?",
                "cavablar": ["A) E_k = m * v", "B) E_k = 1/2 * m * v^2", "C) E_k = m * g * h"],
                "dogru_cavab": "B) E_k = 1/2 * m * v^2"
            }

        }
        self.control(self.fizika_suallari)
    def azerbaycan(self):
        print('#' * 50)
        print('--------------AZƏRBAYCAN-DİLİ---------------')
        self.azerbaycan_dili_suallari = {
            1: {
                "sual": "Azərbaycan dilində ən çox istifadə olunan samit səs hansıdır?",
                "cavablar": ["A) M", "B) N", "C) S"],
                "dogru_cavab": "B) N"
            },
            2: {
                "sual": "Azərbaycan dilində neçə sait səs var?",
                "cavablar": ["A) 6", "B) 8", "C) 10"],
                "dogru_cavab": "A) 6"
            },
            3: {
                "sual": "Ən çox istifadə olunan şəkilçilər hansılardır?",
                "cavablar": ["A) Yekun şəkilçiləri", "B) Qoşulma şəkilçiləri", "C) Birləşmə şəkilçiləri"],
                "dogru_cavab": "B) Qoşulma şəkilçiləri"
            }

        }

        self.control(self.azerbaycan_dili_suallari)

    def cografiya(self):
        print('#' * 50)
        print('--------------COĞRAFİA---------------')
        self.cografiya_suallari = {
            1: {
                "sual": "Dünyanın ən böyük okeanı hansıdır?",
                "cavablar": ["A) Atlantik Okeanı", "B) Sakit Okean", "C) Hind Okeanı"],
                "dogru_cavab": "B) Sakit Okean"
            },
            2: {
                "sual": "Azərbaycanın paytaxtı hansı şəhərdir?",
                "cavablar": ["A) Gəncə", "B) Sumqayıt", "C) Bakı"],
                "dogru_cavab": "C) Bakı"
            },
            3: {
                "sual": "Afrikanın ən böyük ölkəsi hansıdır?",
                "cavablar": ["A) Misir", "B) Nigeriya", "C) Sudan"],
                "dogru_cavab": "B) Nigeriya"
            }

        }
        self.control(self.cografiya_suallari)

    def bialogiya(self):
        print('#' * 50)
        print('--------------BİALOGİYA---------------')
        self.biologiya_suallari = {
            1: {
                "sual": "İnsan bədənindəki ən böyük orqan hansıdır?",
                "cavablar": ["A) Ürək", "B) Dəri", "C) Beyin"],
                "dogru_cavab": "B) Dəri"
            },
            2: {
                "sual": "Fotosintez hansı canlılarda baş verir?",
                "cavablar": ["A) Heyvanlar", "B) Bitkilər", "C) Mikroorqanizmlər"],
                "dogru_cavab": "B) Bitkilər"
            },
            3: {
                "sual": "Mikroskopda görünməyən canlılar hansılardır?",
                "cavablar": ["A) Hüceyrələr", "B) Mikroorqanizmlər", "C) Bakteriyalar"],
                "dogru_cavab": "B) Mikroorqanizmlər"
            }

        }
        self.control(self.biologiya_suallari)

    def tarix(self):
        print('#' * 50)
        print('--------------TARİX---------------')
        tarix_suallari = {
            1: {
                "sual": "Azərbaycanın müstəqilliyini elan etdiyi tarix hansıdır?",
                "cavablar": ["A) 28 May 1918", "B) 30 Avqust 1991", "C) 12 Oktyabr 1920"],
                "dogru_cavab": "A) 28 May 1918"
            },
            2: {
                "sual": "Müasir dövrün ilk döyüş təyyarəsi hansı ölkə tərəfindən istehsal olunmuşdur?",
                "cavablar": ["A) ABŞ", "B) Almaniya", "C) İngiltərə"],
                "dogru_cavab": "A) ABŞ"
            },
            3: {
                "sual": "Azərbaycanın ən böyük müharibəsində iştirak etdiyi dövr hansıdır?",
                "cavablar": ["A) I Dünya Müharibəsi", "B) II Dünya Müharibəsi", "C) Qarabağ Müharibəsi"],
                "dogru_cavab": "B) II Dünya Müharibəsi"
            }

        }
        self.control(self.cografiya_suallari)

    def edebiyyat(self):
        print('#' * 50)
        print('--------------ƏDƏBİYYAT---------------')
        self.edebiyyat_suallari = {
            1: {
                "sual": "Ədəbiyyatımızın ilk yazılı abidəsi hansıdır?",
                "cavablar": ["A) Kitabi-Dədə Qorqud", "B) Dədə Qorqud", "C) Xəmsə"],
                "dogru_cavab": "A) Kitabi-Dədə Qorqud"
            },
            2: {
                "sual": "Əsəri 'Füzuli' tərəfindən yazılan 'Leyli və Mecnun' hansı dövrə aiddir?",
                "cavablar": ["A) XVII əsr", "B) XV əsr", "C) XII əsr"],
                "dogru_cavab": "B) XV əsr"
            },
            3: {
                "sual": "Azərbaycanın xalq şairi, 'Sənsiz' adlı şeirinin müəllifi kimdir?",
                "cavablar": ["A) Nizami Gəncəvi", "B) Məhəmməd Füzuli", "C) Xurşidbanu Natəvan"],
                "dogru_cavab": "C) Xurşidbanu Natəvan"
            }

        }
        self.control(self.edebiyyat_suallari)

    def informatika(self):
        print('#' * 50)
        print('--------------İNFORMATİKA---------------')
        self.informatika_suallari = {
            1: {
                "sual": "İnformatikanın əsas məqsədi nədir?",
                "cavablar": ["A) Məlumatların saxlanması və ötürülməsi", "B) Kompüterləri idarə etmək",
                             "C) Veb səhifə yaratmaq"],
                "dogru_cavab": "A) Məlumatların saxlanması və ötürülməsi"
            },
            2: {
                "sual": "Kompüterin beyni sayılan vahid hansıdır?",
                "cavablar": ["A) CPU", "B) RAM", "C) Hard disk"],
                "dogru_cavab": "A) CPU"
            },
            3: {
                "sual": "Ən böyük məlumat saxlama vahidi hansıdır?",
                "cavablar": ["A) Byte", "B) Terabayt", "C) Gigabayt"],
                "dogru_cavab": "B) Terabayt"
            }

        }
        self.control(self.informatika_suallari)


    def start(self):

        print("\n***İMTAHANA*** Xos gelmisiniz!!")

        while True:
            self.secim = input("Zehmet olmasa qrupunuzu qeyd edin.")

            if self.secim.isdigit() and self.secim != "":
                if int(self.secim) >= 1 and int(self.secim) <= 5:

                    if self.secim == '1':
                        self.qrup_1()
                        break
                    elif self.secim == '2':
                        self.qrup_2()
                        break
                    elif self.secim == '3':
                        self.qrup_3()
                        break
                    elif self.secim == '4':
                        self.qrup_4()
                        break
                    elif self.secim == '5':
                        self.qrup_5()
                        break
                else:
                    print(f"{self.secim} düzgün seçim deyil")
                    print("Seçiminiz 1-dən 5-ə qədər olmalıdır.")

            else:
                print(f"{self.secim} düzgün seçim deyil")
                print("Seçiminizi düzgün edin")

    def menu(self):
        while True:
            self.start = input('Yenidən cəhd etmək istərdinizmi? [-hə- enter, -yox- < Q > duyməsini basın!')
            if self.start.lower() == 'Q' :
                print('\nSizinlə vaxt keçirmək çox xoş oldu  Sağolun!!!')
                sys.exit()

            elif self.secim.strip() == '' or self.start.isdigit():

                print("\nXahiş edirəm düzgün bir seçim daxil edin (boş və ya rəqəm olmamalıdır).")
            else:
                SualCavabOyunu()


ders = SualCavabOyunu()
