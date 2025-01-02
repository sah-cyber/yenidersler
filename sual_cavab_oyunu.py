import sys


class SualCavabOyunu:

    def __init__(self):
        self.dogru_cavab = 0
        self.sef_cavab = 0
        self.cavab_bend = ['A', 'B', 'C']
        self.start()
        print()

    def qrup_1(self):
        print('*' * 50)
        print('1-ci qrup üzrə Fennler')
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
        print('2-ci qrup üzrə Fennler')
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
        print('3-cü qrup üzrə Fennler')
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
        print('4-cü qrup üzrə Fennler')
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
        print('5-ci qrup üzrə Fennler')
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
            self.kecid_bal = (self.dogru_cavab *5)- (self.sef_cavab*2)
            print('Sizin keçid balınız',self.kecid_bal)
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
            },
            4: {
                "sual": "Какое слово является существительным?",
                "cavablar": ["A) Книга", "B) Быстро", "C) Плавать"],
                "dogru_cavab": "A) Книга"
            },
            5: {
                "sual": "Как называется самый большой океан на Земле?",
                "cavablar": ["A) Атлантический океан", "B) Тихий океан", "C) Индийский океан"],
                "dogru_cavab": "B) Тихий океан"
            },
            6: {
                "sual": "Сколько месяцев в году?",
                "cavablar": ["A) 10", "B) 12", "C) 14"],
                "dogru_cavab": "B) 12"
            },
            7: {
                "sual": "Какой элемент таблицы Менделеева имеет символ 'O'?",
                "cavablar": ["A) Золото", "B) Водород", "C) Кислород"],
                "dogru_cavab": "C) Кислород"
            },
            8: {
                "sual": "Какая планета ближе всего к Солнцу?",
                "cavablar": ["A) Земля", "B) Венера", "C) Меркурий"],
                "dogru_cavab": "C) Меркурий"
            },
            9: {
                "sual": "Какое число является простым?",
                "cavablar": ["A) 15", "B) 7", "C) 20"],
                "dogru_cavab": "B) 7"
            },
            10: {
                "sual": "Какой цвет флага России?",
                "cavablar": ["A) Зеленый, белый, красный", "B) Белый, синий, красный", "C) Желтый, синий, красный"],
                "dogru_cavab": "B) Белый, синий, красный"
            },
            11: {
                "sual": "Как называется процесс превращения воды в пар?",
                "cavablar": ["A) Конденсация", "B) Испарение", "C) Замерзание"],
                "dogru_cavab": "B) Испарение"
            },
            12: {
                "sual": "Как называется первый месяц года?",
                "cavablar": ["A) Январь", "B) Февраль", "C) Декабрь"],
                "dogru_cavab": "A) Январь"
            },
            13: {
                "sual": "Какая река является самой длинной в мире?",
                "cavablar": ["A) Нил", "B) Амазонка", "C) Янцзы"],
                "dogru_cavab": "A) Нил"
            },
            14: {
                "sual": "Какое государство является самым большим по площади?",
                "cavablar": ["A) США", "B) Китай", "C) Россия"],
                "dogru_cavab": "C) Россия"
            },
            15: {
                "sual": "Какой металл имеет символ 'Fe'?",
                "cavablar": ["A) Золото", "B) Железо", "C) Медь"],
                "dogru_cavab": "B) Железо"
            }
        }
        self.control(self.rus_dict_questions)

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
            },
            4: {
                "sual": "Quelle est la langue officielle de la France ?",
                "cavablar": ["A) Espagnol", "B) Anglais", "C) Français"],
                "dogru_cavab": "C) Français"
            },
            5: {
                "sual": "Quel est le plus grand pays du monde ?",
                "cavablar": ["A) Chine", "B) Russie", "C) États-Unis"],
                "dogru_cavab": "B) Russie"
            },
            6: {
                "sual": "Qui a écrit 'Les Misérables' ?",
                "cavablar": ["A) Victor Hugo", "B) Emile Zola", "C) Marcel Proust"],
                "dogru_cavab": "A) Victor Hugo"
            },
            7: {
                "sual": "Quel est le symbole chimique de l'eau ?",
                "cavablar": ["A) O2", "B) H2O", "C) CO2"],
                "dogru_cavab": "B) H2O"
            },
            8: {
                "sual": "Combien de continents y a-t-il sur Terre ?",
                "cavablar": ["A) 5", "B) 6", "C) 7"],
                "dogru_cavab": "C) 7"
            },
            9: {
                "sual": "Quel est le plus grand fleuve de France ?",
                "cavablar": ["A) La Seine", "B) La Loire", "C) Le Rhône"],
                "dogru_cavab": "B) La Loire"
            },
            10: {
                "sual": "Quelle est la monnaie utilisée en France ?",
                "cavablar": ["A) Euro", "B) Dollar", "C) Livre"],
                "dogru_cavab": "A) Euro"
            },
            11: {
                "sual": "Quel est le plus grand désert du monde ?",
                "cavablar": ["A) Le désert du Sahara", "B) Le désert de Gobi", "C) L'Antarctique"],
                "dogru_cavab": "C) L'Antarctique"
            },
            12: {
                "sual": "Quel est le plus grand animal terrestre ?",
                "cavablar": ["A) L'éléphant", "B) La baleine bleue", "C) Le rhinocéros"],
                "dogru_cavab": "A) L'éléphant"
            },
            13: {
                "sual": "Combien de pays composent l'Union Européenne ?",
                "cavablar": ["A) 27", "B) 28", "C) 30"],
                "dogru_cavab": "A) 27"
            },
            14: {
                "sual": "Qui a peint la Joconde ?",
                "cavablar": ["A) Pablo Picasso", "B) Claude Monet", "C) Léonard de Vinci"],
                "dogru_cavab": "C) Léonard de Vinci"
            },
            15: {
                "sual": "Quel est l'élément chimique avec le symbole 'Fe' ?",
                "cavablar": ["A) Fer", "B) Argent", "C) Or"],
                "dogru_cavab": "A) Fer"
            }
        }
        self.control(self.fransiz_dict_questions)

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
            },
            4: {
                "sual": "Wer war der erste Bundeskanzler der Bundesrepublik Deutschland?",
                "cavablar": ["A) Willy Brandt", "B) Konrad Adenauer", "C) Angela Merkel"],
                "dogru_cavab": "B) Konrad Adenauer"
            },
            5: {
                "sual": "Welches Land grenzt nicht an Deutschland?",
                "cavablar": ["A) Frankreich", "B) Polen", "C) Italien"],
                "dogru_cavab": "C) Italien"
            },
            6: {
                "sual": "Welches Bundesland hat die größte Fläche?",
                "cavablar": ["A) Bayern", "B) Nordrhein-Westfalen", "C) Niedersachsen"],
                "dogru_cavab": "A) Bayern"
            },
            7: {
                "sual": "Welches ist das größte Land Europas?",
                "cavablar": ["A) Frankreich", "B) Deutschland", "C) Russland"],
                "dogru_cavab": "C) Russland"
            },
            8: {
                "sual": "Wie viele Sterne befinden sich auf der Flagge der Europäischen Union?",
                "cavablar": ["A) 12", "B) 15", "C) 10"],
                "dogru_cavab": "A) 12"
            },
            9: {
                "sual": "Welche Stadt ist die größte in Deutschland?",
                "cavablar": ["A) Berlin", "B) München", "C) Hamburg"],
                "dogru_cavab": "A) Berlin"
            },
            10: {
                "sual": "Wer ist der Autor von 'Faust'?",
                "cavablar": ["A) Johann Wolfgang von Goethe", "B) Friedrich Schiller", "C) Thomas Mann"],
                "dogru_cavab": "A) Johann Wolfgang von Goethe"
            },
            11: {
                "sual": "Welches Tier ist das Wappentier von Deutschland?",
                "cavablar": ["A) Adler", "B) Löwe", "C) Bär"],
                "dogru_cavab": "A) Adler"
            },
            12: {
                "sual": "Welches war das erste Bundesland, das der Bundesrepublik Deutschland beitrat?",
                "cavablar": ["A) Hessen", "B) Bayern", "C) Baden-Württemberg"],
                "dogru_cavab": "A) Hessen"
            },
            13: {
                "sual": "Welche deutsche Stadt ist berühmt für ihre Erfinder und das Automobil?",
                "cavablar": ["A) Stuttgart", "B) Frankfurt", "C) Köln"],
                "dogru_cavab": "A) Stuttgart"
            },
            14: {
                "sual": "Wie heißt der deutsche Nationalfeiertag?",
                "cavablar": ["A) Tag der Deutschen Einheit", "B) Oktoberfest", "C) Weihnachten"],
                "dogru_cavab": "A) Tag der Deutschen Einheit"
            },
            15: {
                "sual": "Wie heißt der bekannteste deutsche Komponist, der die 'Ode an die Freude' komponierte?",
                "cavablar": ["A) Johann Sebastian Bach", "B) Ludwig van Beethoven", "C) Wolfgang Amadeus Mozart"],
                "dogru_cavab": "B) Ludwig van Beethoven"
            }
        }
        self.control(self.alman_dict_questions)

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
            },
            4: {
                "sual": "Aşağıdakilerden hansısı mülkiyyət zamiridir?",
                "cavablar": ["A) Her", "B) She", "C) Hers"],
                "dogru_cavab": "C) Hers"
            },
            5: {
                "sual": "'Go' sözünün keçmiş zaman forması hansıdır?",
                "cavablar": ["A) Went", "B) Gone", "C) Going"],
                "dogru_cavab": "A) Went"
            },
            6: {
                "sual": "Aşağıdakilerden hansısı sifətdir?",
                "cavablar": ["A) Beautiful", "B) Running", "C) Quickly"],
                "dogru_cavab": "A) Beautiful"
            },
            7: {
                "sual": "'They ______ at home.' cümləsində doğru fel forması nədir?",
                "cavablar": ["A) Are", "B) Is", "C) Am"],
                "dogru_cavab": "A) Are"
            },
            8: {
                "sual": "Aşağıdakilerden hansısı 'happy' sözünün sinonimidir?",
                "cavablar": ["A) Sad", "B) Joyful", "C) Angry"],
                "dogru_cavab": "B) Joyful"
            },
            9: {
                "sual": "'Big' sözünün ziddi hansıdır?",
                "cavablar": ["A) Small", "B) Tall", "C) Heavy"],
                "dogru_cavab": "A) Small"
            },
            10: {
                "sual": "'She ______ to the store' cümləsinin doğru forması hansıdır?",
                "cavablar": ["A) Goes", "B) Going", "C) Go"],
                "dogru_cavab": "A) Goes"
            },
            11: {
                "sual": "'The cat sleeps on the mat' cümləsində subyekt nədir?",
                "cavablar": ["A) Sleeps", "B) The mat", "C) The cat"],
                "dogru_cavab": "C) The cat"
            },
            12: {
                "sual": "Aşağıdakilerden hansı bağlayıcı sözüdür?",
                "cavablar": ["A) But", "B) Quickly", "C) Walk"],
                "dogru_cavab": "A) But"
            },
            13: {
                "sual": "'Child' sözünün doğru çoxluq forması nədir?",
                "cavablar": ["A) Childs", "B) Children", "C) Childes"],
                "dogru_cavab": "B) Children"
            },
            14: {
                "sual": "Aşağıdakilerden hansı gələcək zaman formasıdır?",
                "cavablar": ["A) She will go to the store.", "B) She goes to the store.", "C) She went to the store."],
                "dogru_cavab": "A) She will go to the store."
            },
            15: {
                "sual": "Aşağıdakilerden hansı qoşma sözüdür?",
                "cavablar": ["A) But", "B) Quickly", "C) Walk"],
                "dogru_cavab": "A) But"
            }
        }

        self.control(self.english_dict_questions_azerbaijani)



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
            },
            4: {
                "sual": "Aşağıdakı maddələrdən hansı asidik xarakterə malikdir?",
                "cavablar": ["A) Su", "B) Sirkə", "C) Soda"],
                "dogru_cavab": "B) Sirkə"
            },
            5: {
                "sual": "Kimyəvi reaksiyalarda enerji dəyişməsini ölçən cihazın adı nədir?",
                "cavablar": ["A) Termometr", "B) Kalorimetr", "C) Barometr"],
                "dogru_cavab": "B) Kalorimetr"
            },
            6: {
                "sual": "Hidrogenlə reaksiya verərək su meydana gətirən metal hansı metal olacaq?",
                "cavablar": ["A) Kükürd", "B) Alüminium", "C) Natrium"],
                "dogru_cavab": "C) Natrium"
            },
            7: {
                "sual": "Aşağıdakı maddələrdən hansı birləşmədir?",
                "cavablar": ["A) Oksigen", "B) Helyum", "C) Su (H2O)"],
                "dogru_cavab": "C) Su (H2O)"
            },
            8: {
                "sual": "Bütün atomların tərkibində olan əsas hissəcik hansıdır?",
                "cavablar": ["A) Proton", "B) Elektron", "C) Neutron"],
                "dogru_cavab": "B) Elektron"
            },
            9: {
                "sual": "Kimyəvi elementlərin yerləşdiyi cədvəlin adı nədir?",
                "cavablar": ["A) Dövri Cədvəl", "B) Kimyəvi Cədvəl", "C) Elementlər Cədvəli"],
                "dogru_cavab": "A) Dövri Cədvəl"
            },
            10: {
                "sual": "Hansı maddə qaz halında sıxıla bilər?",
                "cavablar": ["A) Su", "B) Oksigen", "C) Dəmir"],
                "dogru_cavab": "B) Oksigen"
            },
            11: {
                "sual": "Qazların həcmi ilə təzyiqi arasındakı əlaqəni göstərən qanun hansıdır?",
                "cavablar": ["A) Boyle qanunu", "B) Charles qanunu", "C) Avogadro qanunu"],
                "dogru_cavab": "A) Boyle qanunu"
            },
            12: {
                "sual": "Kimyada bir maddənin suya olan həllini ölçmək üçün istifadə olunan cihaz hansıdır?",
                "cavablar": ["A) Refraktometr", "B) Spektrofotometr", "C) pH-metr"],
                "dogru_cavab": "C) pH-metr"
            },
            13: {
                "sual": "Aşağıdakilerden hangi bir elementin ismi doğru yazılmıştır?",
                "cavablar": ["A) Kükürdlə", "B) Karbon", "C) Karbona"],
                "dogru_cavab": "B) Karbon"
            },
            14: {
                "sual": "Kalsium karbonat (CaCO3) hansı maddələrdən əmələ gəlir?",
                "cavablar": ["A) Kalsium və karbon dioksid", "B) Kalsium və oksigen", "C) Kalsium, karbon və oksigen"],
                "dogru_cavab": "C) Kalsium, karbon və oksigen"
            },
            15: {
                "sual": "Kimyada maddələrin oksidləşməsi nəyi bildirir?",
                "cavablar": ["A) Elektron verməsi", "B) Elektron qəbul etməsi", "C) Molekul halında mövcud olması"],
                "dogru_cavab": "A) Elektron verməsi"
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
            },
            4: {
                "sual": "5x + 3 = 18 tənliyini həll edin.",
                "cavablar": ["A) x = 3", "B) x = 4", "C) x = 2"],
                "dogru_cavab": "A) x = 3"
            },
            5: {
                "sual": "Bir dairənin radiusu 7 sm-dir. Dairənin sahəsini tapın. (π ≈ 3.14)",
                "cavablar": ["A) 153.94 sm²", "B) 49 sm²", "C) 25 sm²"],
                "dogru_cavab": "A) 153.94 sm²"
            },
            6: {
                "sual": "Bir kvadratın tərəfi 8 sm-dir. Kvadratın perimetri nə qədərdir?",
                "cavablar": ["A) 32 sm", "B) 16 sm", "C) 64 sm"],
                "dogru_cavab": "A) 32 sm"
            },
            7: {
                "sual": "Bir düzbucaqlı paralelepipedin həcmi 360 sm³, eni 6 sm, hündürlüyü isə 5 sm-dir. Uzunluğu tapın.",
                "cavablar": ["A) 12 sm", "B) 10 sm", "C) 15 sm"],
                "dogru_cavab": "B) 12 sm"
            },
            8: {
                "sual": "Bir üçbucağın sahəsi 30 sm², hündürlüyü 6 sm-dir. Üçbucağın əsasını tapın.",
                "cavablar": ["A) 5 sm", "B) 10 sm", "C) 6 sm"],
                "dogru_cavab": "B) 10 sm"
            },
            9: {
                "sual": "Bir kəsirin ədədi 12, məxrəci isə 8-dir. Kəsirin sadə halı necə olacaq?",
                "cavablar": ["A) 3/2", "B) 4/3", "C) 2/3"],
                "dogru_cavab": "A) 3/2"
            },
            10: {
                "sual": "x² - 5x + 6 = 0 tənliyini həll edin.",
                "cavablar": ["A) x = 2, x = 3", "B) x = 1, x = 6", "C) x = 0, x = 6"],
                "dogru_cavab": "A) x = 2, x = 3"
            },
            11: {
                "sual": "Bir düz xəttin tərsini tapmaq üçün hansı əməliyyatı aparmaq lazımdır?",
                "cavablar": ["A) Toplama", "B) Çıxma", "C) Bölmə"],
                "dogru_cavab": "C) Bölmə"
            },
            12: {
                "sual": "Bir cəbrik ifadənin qüvvətindəki əsas necə ifadə edilir?",
                "cavablar": ["A) Təsadüfi ədəd", "B) İfadənin baza ədədidir", "C) İfadənin nəticəsidir"],
                "dogru_cavab": "B) İfadənin baza ədədidir"
            },
            13: {
                "sual": "Bir ədədin yüzdə 20-si 50-dir. Ədədin özü nə qədərdir?",
                "cavablar": ["A) 250", "B) 200", "C) 100"],
                "dogru_cavab": "B) 200"
            },
            14: {
                "sual": "Bir kvadratın sahəsi 64 sm²-dir. Kvadratın tərəfi nə qədərdir?",
                "cavablar": ["A) 8 sm", "B) 4 sm", "C) 16 sm"],
                "dogru_cavab": "A) 8 sm"
            },
            15: {
                "sual": "Bir cəm 50-dir. Əgər birinci ədəd 30, ikinci ədəd isə 20-dirsə, bu iki ədədin fərqi nə qədərdir?",
                "cavablar": ["A) 10", "B) 5", "C) 20"],
                "dogru_cavab": "A) 10"
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
            },
            4: {
                "sual": "Elektrik cərəyanının istiqaməti necə müəyyən olunur?",
                "cavablar": ["A) Elektronların hərəkət istiqamətinə görə",
                             "B) Cərəyanın keçiricilərinin hərəkətinə görə", "C) Yüklərin hərəkət istiqamətinə görə"],
                "dogru_cavab": "C) Yüklərin hərəkət istiqamətinə görə"
            },
            5: {
                "sual": "Bir cismin sürətini artırmaq üçün hansı amil artırılmalıdır?",
                "cavablar": ["A) Kütlə", "B) Qüvvə", "C) Həcm"],
                "dogru_cavab": "B) Qüvvə"
            },
            6: {
                "sual": "Bir cismə tətbiq edilən qüvvə nəyi dəyişdirir?",
                "cavablar": ["A) Sürətini", "B) Kütləsini", "C) Həcmini"],
                "dogru_cavab": "A) Sürətini"
            },
            7: {
                "sual": "Fizikada iş necə ölçülür?",
                "cavablar": ["A) Enerji", "B) Güc", "C) Güc * zaman"],
                "dogru_cavab": "A) Enerji"
            },
            8: {
                "sual": "Bir cismi yerə atdıqda hansı enerji artır?",
                "cavablar": ["A) Kinetik enerji", "B) Potensial enerji", "C) İstilik enerjisi"],
                "dogru_cavab": "B) Potensial enerji"
            },
            9: {
                "sual": "Bir maddənin sıxlığını necə hesablayırıq?",
                "cavablar": ["A) Həcm / Kütlə", "B) Kütlə / Həcm", "C) Kütlə * Həcm"],
                "dogru_cavab": "B) Kütlə / Həcm"
            },
            10: {
                "sual": "Bir cismin sürətini necə ölçürük?",
                "cavablar": ["A) Termometrlə", "B) Tachometrlə", "C) Sürət ölçən aparatla"],
                "dogru_cavab": "C) Sürət ölçən aparatla"
            },
            11: {
                "sual": "Elektrik cərəyanının ölçü vahidi nədir?",
                "cavablar": ["A) Volt", "B) Amper", "C) Ohm"],
                "dogru_cavab": "B) Amper"
            },
            12: {
                "sual": "Termometrlə ölçülən fiziki böyüklük hansıdır?",
                "cavablar": ["A) Sıxlıq", "B) Temperatur", "C) Təbii işıq"],
                "dogru_cavab": "B) Temperatur"
            },
            13: {
                "sual": "Bir cismin hərəkətinin dəyişməsi hansı qanuna əsaslanır?",
                "cavablar": ["A) Newton-un ikinci qanunu", "B) Newton-un birinci qanunu", "C) Enerji qorunumu qanunu"],
                "dogru_cavab": "A) Newton-un ikinci qanunu"
            },
            14: {
                "sual": "Bir cismə tətbiq edilən qüvvə ilə sürət arasındakı əlaqəni nə göstərir?",
                "cavablar": ["A) Kinetik enerji", "B) Newton-un birinci qanunu", "C) Newton-un ikinci qanunu"],
                "dogru_cavab": "C) Newton-un ikinci qanunu"
            },
            15: {
                "sual": "Bir maddə maye halda olduqda hansı xüsusiyyətə malikdir?",
                "cavablar": ["A) Kütləsi sabitdir, amma şəkli dəyişir", "B) Həcm və şəkil dəyişir",
                             "C) Şəkli dəyişir, amma həcmi sabitdir"],
                "dogru_cavab": "C) Şəkli dəyişir, amma həcmi sabitdir"
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
            },
            4: {
                "sual": "Azərbaycan dilində neçə sifət var?",
                "cavablar": ["A) 4", "B) 3", "C) 2"],
                "dogru_cavab": "A) 4"
            },
            5: {
                "sual": "Sözün kökünü tapın: 'yazılı'",
                "cavablar": ["A) Yaz", "B) Yazi", "C) Yazı"],
                "dogru_cavab": "A) Yaz"
            },
            6: {
                "sual": "Hansı cümlə xəbərsiz cümlədir?",
                "cavablar": ["A) Məni görüb dur", "B) Gəlirəm", "C) O mənim dostumdur"],
                "dogru_cavab": "C) O mənim dostumdur"
            },
            7: {
                "sual": "Aşağıdakılardan hansı ifadə kəlamdır?",
                "cavablar": ["A) Mən evə gedirəm", "B) Evə getdim", "C) Evə gedən", ],
                "dogru_cavab": "A) Mən evə gedirəm"
            },
            8: {
                "sual": "Azərbaycan dilində hansı növ cümlə təklif cümləsidir?",
                "cavablar": ["A) Sənin üçün yaxşı olacaq", "B) Mən dərsləri oxuyuram", "C) Bunu oxu"],
                "dogru_cavab": "C) Bunu oxu"
            },
            9: {
                "sual": "Azərbaycan dilində 'cək' şəkilçisi hansı mənanı bildirir?",
                "cavablar": ["A) Məcburiyyət", "B) Hərəkət", "C) Hərəkət etmək"],
                "dogru_cavab": "A) Məcburiyyət"
            },
            10: {
                "sual": "Aşağıdakılardan hansı söz birləşməsidir?",
                "cavablar": ["A) Böyük ev", "B) Evdə oturmaq", "C) Hava şəraiti"],
                "dogru_cavab": "A) Böyük ev"
            },
            11: {
                "sual": "Azərbaycan dilində hansı növ feilə aid şəxs şəkilçisi yoxdur?",
                "cavablar": ["A) İlk şəxs", "B) Üçüncü şəxs", "C) Dördüncü şəxs"],
                "dogru_cavab": "C) Dördüncü şəxs"
            },
            12: {
                "sual": "Birləşmə şəkilçisi nəyi bildirir?",
                "cavablar": ["A) Hərəkət", "B) Məqsəd", "C) Hərəkət və səbəb"],
                "dogru_cavab": "B) Məqsəd"
            },
            13: {
                "sual": "Azərbaycan dilində hansı cümlə tamamlayıcıdır?",
                "cavablar": ["A) Mən səni tanıdım", "B) Mən dərslərimi oxuyuram", "C) Mən evə getdim"],
                "dogru_cavab": "B) Mən dərslərimi oxuyuram"
            },
            14: {
                "sual": "Yuxarıdakı cümlənin hansı növü xəbər cümləsidir? 'O evə gedir.'",
                "cavablar": ["A) Müstəqil", "B) İstiqamətli", "C) Cümlə"],
                "dogru_cavab": "A) Müstəqil"
            },
            15: {
                "sual": "Aşağıdakılardan hansı cümlə sorğu cümləsidir?",
                "cavablar": ["A) Mən hər gün kitab oxuyuram", "B) Nə vaxt gəlirsən?", "C) Gəlməliyəm"],
                "dogru_cavab": "B) Nə vaxt gəlirsən?"
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
            },
            4: {
                "sual": "Dünyada ən uzun çay hansıdır?",
                "cavablar": ["A) Amazon", "B) Nil", "C) Yangtze"],
                "dogru_cavab": "B) Nil"
            },
            5: {
                "sual": "Hansı ölkə Asiyanın ən böyük ölkəsidir?",
                "cavablar": ["A) Çin", "B) Hindistan", "C) Rusiya"],
                "dogru_cavab": "A) Çin"
            },
            6: {
                "sual": "Təbiətdə 'Yağış meşəsi' bölgəsi harada yerləşir?",
                "cavablar": ["A) Amazon", "B) Səhra", "C) Arktik"],
                "dogru_cavab": "A) Amazon"
            },
            7: {
                "sual": "İqlim növlərindən hansıdır subtropik iqlimə aiddir?",
                "cavablar": ["A) Ekvatordan yaxın", "B) Sahil zonaları", "C) Hündür dağlar"],
                "dogru_cavab": "B) Sahil zonaları"
            },
            8: {
                "sual": "İqlimlərdə ən çox rast gəlinən atmosfer hadisəsi hansıdır?",
                "cavablar": ["A) Qasırğa", "B) Yağış", "C) Qar"],
                "dogru_cavab": "B) Yağış"
            },
            9: {
                "sual": "Çin Xalq Respublikasının əsas dağ sistemi hansıdır?",
                "cavablar": ["A) Himalay", "B) Altay", "C) Tien Şan"],
                "dogru_cavab": "A) Himalay"
            },
            10: {
                "sual": "Dünyanın ən yüksək dağı hansıdır?",
                "cavablar": ["A) K2", "B) Everest", "C) Makalu"],
                "dogru_cavab": "B) Everest"
            },
            11: {
                "sual": "Hansı çay Afrikada yerləşir?",
                "cavablar": ["A) Niger", "B) Nil", "C) Amazon"],
                "dogru_cavab": "B) Nil"
            },
            12: {
                "sual": "Ən böyük adalar qrupunun adı nədir?",
                "cavablar": ["A) Maldiv adaları", "B) Japon adaları", "C) İslandiya adaları"],
                "dogru_cavab": "B) Japon adaları"
            },
            13: {
                "sual": "Şimal yarımkürəsində yerləşən ölkələrdən hansı ən çox şimalda yerləşir?",
                "cavablar": ["A) Kanada", "B) Rusya", "C) Finlandiya"],
                "dogru_cavab": "B) Rusya"
            },
            14: {
                "sual": "Hansı ölkə Avstraliya ilə ən yaxın qitədir?",
                "cavablar": ["A) Hindistan", "B) Çili", "C) Yeni Zelandiya"],
                "dogru_cavab": "A) Hindistan"
            },
            15: {
                "sual": "Səhra iqlimi hansı regionda yayılıb?",
                "cavablar": ["A) Asiya", "B) Afrika", "C) Avstraliya"],
                "dogru_cavab": "B) Afrika"
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
            },
            4: {
                "sual": "Hüceyrə nə ilə əhatə olunur?",
                "cavablar": ["A) Hüceyrə divarı", "B) Hüceyrə membranı", "C) Yad cisimlər"],
                "dogru_cavab": "B) Hüceyrə membranı"
            },
            5: {
                "sual": "Xlorofilin əsas funksiyası nədir?",
                "cavablar": ["A) Yaradıcı enerji saxlamaq", "B) Fotosintez üçün işıq enerjisini udmaq",
                             "C) Oksigen istehsal etmək"],
                "dogru_cavab": "B) Fotosintez üçün işıq enerjisini udmaq"
            },
            6: {
                "sual": "Hansı orqanizm fotosintez prosesini həyata keçirir?",
                "cavablar": ["A) İnsan", "B) Bitki", "C) Heyvan"],
                "dogru_cavab": "B) Bitki"
            },
            7: {
                "sual": "Qan dövranı hansı orqan vasitəsilə həyata keçirilir?",
                "cavablar": ["A) Ağciyər", "B) Ürək", "C) Qaraciyər"],
                "dogru_cavab": "B) Ürək"
            },
            8: {
                "sual": "Ağ qan hüceyrələrinin əsas funksiyası nədir?",
                "cavablar": ["A) Oksigen daşımaq", "B) İmmunitet müdafiəsi", "C) Qida emalı"],
                "dogru_cavab": "B) İmmunitet müdafiəsi"
            },
            9: {
                "sual": "Hansı orqanizm özünü çoxalda bilməz?",
                "cavablar": ["A) İnsan", "B) Bakteriya", "C) Bitki"],
                "dogru_cavab": "A) İnsan"
            },
            10: {
                "sual": "İnsan bədənində D vitamini hansı orqanda sintez olunur?",
                "cavablar": ["A) Böyrəklər", "B) Dəri", "C) Qaraciyər"],
                "dogru_cavab": "B) Dəri"
            },
            11: {
                "sual": "Qan şəkərinin nəzarəti ilə məşğul olan orqan hansıdır?",
                "cavablar": ["A) Böyrək", "B) Qaraciyər", "C) Pankreas"],
                "dogru_cavab": "C) Pankreas"
            },
            12: {
                "sual": "Ən çox yayılan qida maddəsi hansıdır?",
                "cavablar": ["A) Zülallar", "B) Karbohidratlar", "C) Yağlar"],
                "dogru_cavab": "B) Karbohidratlar"
            },
            13: {
                "sual": "Evolusiya nəzəriyyəsinin əsasını qoyan alim kimdir?",
                "cavablar": ["A) Charles Darwin", "B) Isaac Newton", "C) Albert Einstein"],
                "dogru_cavab": "A) Charles Darwin"
            },
            14: {
                "sual": "Hansı hüceyrə tipi çoxalmadan əvvəl iki dəfə bölünür?",
                "cavablar": ["A) Sperm hüceyrəsi", "B) Toxuma hüceyrəsi", "C) Yumurtalıq hüceyrəsi"],
                "dogru_cavab": "A) Sperm hüceyrəsi"
            },
            15: {
                "sual": "Hansı canlının həyatı su altında baş verir?",
                "cavablar": ["A) Balıq", "B) Qartal", "C) Aslan"],
                "dogru_cavab": "A) Balıq"
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
            },
            4: {
                "sual": "Cümhuriyyət dövründə Azərbaycan Respublikasının ilk baş naziri kim olmuşdur?",
                "cavablar": ["A) Məhəmməd Əmin Rəsulzadə", "B) Fətəli Xan Xoyski", "C) Nəsib bəy Yusifbəyli"],
                "dogru_cavab": "B) Fətəli Xan Xoyski"
            },
            5: {
                "sual": "Dünya tarixində ilk dəfə olaraq parlamentli sistemin tətbiq olunduğu ölkə hansıdır?",
                "cavablar": ["A) ABŞ", "B) Böyük Britaniya", "C) Fransa"],
                "dogru_cavab": "B) Böyük Britaniya"
            },
            6: {
                "sual": "Türkiyə Respublikası hansı ildə qurulmuşdur?",
                "cavablar": ["A) 1920", "B) 1923", "C) 1919"],
                "dogru_cavab": "B) 1923"
            },
            7: {
                "sual": "Məğlub olan İspaniya, 1492-ci ildə hansı ərazilərini itirdi?",
                "cavablar": ["A) Şimali Afrika", "B) Rusiya", "C) İtaliya"],
                "dogru_cavab": "A) Şimali Afrika"
            },
            8: {
                "sual": "Rusiya imperatorluğunun ilk çarını kim olmuşdur?",
                "cavablar": ["A) İvan IV", "B) Peter I", "C) Yekaterina II"],
                "dogru_cavab": "A) İvan IV"
            },
            9: {
                "sual": "Roma İmperiyasının iki hissəyə ayrılması hansı tarixdə baş vermişdir?",
                "cavablar": ["A) 395", "B) 410", "C) 476"],
                "dogru_cavab": "A) 395"
            },
            10: {
                "sual": "Qədim Misir mədəniyyətinin inkişaf etdiyi çay hansı çaydır?",
                "cavablar": ["A) Nil", "B) Tigris", "C) Fırat"],
                "dogru_cavab": "A) Nil"
            },
            11: {
                "sual": "I Dünya Müharibəsinin başlandığı tarix hansıdır?",
                "cavablar": ["A) 28 İyun 1914", "B) 1 Sentyabr 1914", "C) 11 Noyabr 1918"],
                "dogru_cavab": "A) 28 İyun 1914"
            },
            12: {
                "sual": "Napoleon Bonapartın rəhbərlik etdiyi Fransa hansı dövrdə güclü bir imperiya olmuşdur?",
                "cavablar": ["A) XVII əsr", "B) XVIII əsr", "C) XIX əsr"],
                "dogru_cavab": "C) XIX əsr"
            },
            13: {
                "sual": "Sovet İttifaqının dağılmasının rəsmi olaraq baş verdiyi il hansıdır?",
                "cavablar": ["A) 1989", "B) 1991", "C) 1990"],
                "dogru_cavab": "B) 1991"
            },
            14: {
                "sual": "Müasir dövrün ilk müstəqil dövləti hansı olmuşdur?",
                "cavablar": ["A) ABŞ", "B) Fransız inqilabı", "C) Bolqarıstan"],
                "dogru_cavab": "A) ABŞ"
            },
            15: {
                "sual": "Azərbaycanın Qarabağ bölgəsi hansı tarixi dövrdə zəbt edilmişdir?",
                "cavablar": ["A) 1990-cı illər", "B) 1813-cü il", "C) 1923-cü il"],
                "dogru_cavab": "B) 1813-cü il"
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
            },
            4: {
                "sual": "Nizami Gəncəvi hansı janrda əsərlər yaratmışdır?",
                "cavablar": ["A) Dramanın janrında", "B) Epik şeirdə", "C) Sonnetlərin janrında"],
                "dogru_cavab": "B) Epik şeirdə"
            },
            5: {
                "sual": "'Kəbir' adlı şeiri ilə tanınan və həmçinin 'Divan' adlı əsər yazmış olan məşhur şair kimdir?",
                "cavablar": ["A) Nizami Gəncəvi", "B) Məhəmməd Füzuli", "C) Mirzə Fətəli Axundov"],
                "dogru_cavab": "B) Məhəmməd Füzuli"
            },
            6: {
                "sual": "'Vətən sevgisi' mövzusunu ən çox işləyən Azərbaycan şairi kimdir?",
                "cavablar": ["A) Mirzə Fətəli Axundov", "B) Səməd Vurğun", "C) Məmməd Araz"],
                "dogru_cavab": "B) Səməd Vurğun"
            },
            7: {
                "sual": "Cümhuriyyət dövrünün ilk dram əsəri hansıdır?",
                "cavablar": ["A) Məhəmməd Füzuli – 'Leyli və Mecnun'", "B) Mirzə Fətəli Axundov – 'Hekayə'",
                             "C) Cavid – 'Tənhalıq'"],
                "dogru_cavab": "B) Mirzə Fətəli Axundov – 'Hekayə'"
            },
            8: {
                "sual": "Ədəbiyyatımızda ilk şairlərdən biri olan 'Seyid Azim Şirvani' hansı janrda əsərlər yazmışdır?",
                "cavablar": ["A) Lirik şeir", "B) Fəlsəfi şeir", "C) Hekayə janrı"],
                "dogru_cavab": "A) Lirik şeir"
            },
            9: {
                "sual": "Əsərləri ilə həm klassik, həm də müasir dövrün şəxsiyyətlərinə təsir etmiş, 'Əsli və Kərəm' dastanını yazan şəxs kimdir?",
                "cavablar": ["A) Hüseyn Cavid", "B) Nizami Gəncəvi", "C) Füzuli"],
                "dogru_cavab": "B) Nizami Gəncəvi"
            },
            10: {
                "sual": "Azərbaycanın ən böyük satirik şairlərindən biri olan və 'Hekayə' adlı əsərini yazan kimdir?",
                "cavablar": ["A) Mirzə Fətəli Axundov", "B) Məhəmməd Füzuli", "C) Səməd Vurğun"],
                "dogru_cavab": "A) Mirzə Fətəli Axundov"
            },
            11: {
                "sual": "Azərbaycan ədəbiyyatında 'Qarabağ' mövzusunu işləyən şair kimdir?",
                "cavablar": ["A) Nizami Gəncəvi", "B) Xurşidbanu Natəvan", "C) Füzuli"],
                "dogru_cavab": "B) Xurşidbanu Natəvan"
            },
            12: {
                "sual": "Azərbaycan ədəbiyyatında 'İntibah' dövrünü təmsil edən şair kimdir?",
                "cavablar": ["A) Səməd Vurğun", "B) Məhəmməd Füzuli", "C) Mirzə Fətəli Axundov"],
                "dogru_cavab": "C) Mirzə Fətəli Axundov"
            },
            13: {
                "sual": "Azərbaycan ədəbiyyatında 'Xəmsə' adlı əsəri ilə tanınan şair kimdir?",
                "cavablar": ["A) Mirzə Fətəli Axundov", "B) Məhəmməd Füzuli", "C) Nizami Gəncəvi"],
                "dogru_cavab": "C) Nizami Gəncəvi"
            },
            14: {
                "sual": "Sovet dönəmində Azərbaycanın ən çox oxunan şairi kimdir?",
                "cavablar": ["A) Səməd Vurğun", "B) Rəsul Rza", "C) Mikayıl Müşfiq"],
                "dogru_cavab": "A) Səməd Vurğun"
            },
            15: {
                "sual": "Azərbaycanın ən tanınmış müasir şairlərindən biri olan və 'Yaşamaq istəyirəm' şeirini yazan kimdir?",
                "cavablar": ["A) Rəsul Rza", "B) Mikayıl Müşfiq", "C) Bəxtiyar Vahabzadə"],
                "dogru_cavab": "C) Bəxtiyar Vahabzadə"
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
            },
            4: {
                "sual": "Aşağıdakılardan hansı əməliyyat sisteminə aiddir?",
                "cavablar": ["A) Microsoft Office", "B) Windows", "C) Photoshop"],
                "dogru_cavab": "B) Windows"
            },
            5: {
                "sual": "Bir faylın formatını dəyişdirmək üçün hansı proqram təminatından istifadə olunur?",
                "cavablar": ["A) Web browser", "B) Media player", "C) Konvertor proqramları"],
                "dogru_cavab": "C) Konvertor proqramları"
            },
            6: {
                "sual": "Rəqəmsal məlumatları şifrələmək üçün istifadə olunan üsul hansıdır?",
                "cavablar": ["A) Kriptoqrafiya", "B) Şəbəkə analizi", "C) Şəkil redaktəsi"],
                "dogru_cavab": "A) Kriptoqrafiya"
            },
            7: {
                "sual": "İnternetin ən geniş istifadə olunan protokolu hansıdır?",
                "cavablar": ["A) HTTP", "B) FTP", "C) TCP/IP"],
                "dogru_cavab": "C) TCP/IP"
            },
            8: {
                "sual": "Kompüterdə istifadə olunan operativ yaddaşın adı nədir?",
                "cavablar": ["A) ROM", "B) RAM", "C) Cache"],
                "dogru_cavab": "B) RAM"
            },
            9: {
                "sual": "Şəbəkə üzərindən məlumat ötürülməsini təmin edən alət hansıdır?",
                "cavablar": ["A) Router", "B) Printer", "C) Monitor"],
                "dogru_cavab": "A) Router"
            },
            10: {
                "sual": "Hansı proqramlaşdırma dili veb inkişafında ən çox istifadə olunur?",
                "cavablar": ["A) C++", "B) JavaScript", "C) Python"],
                "dogru_cavab": "B) JavaScript"
            },
            11: {
                "sual": "Aşağıdakılardan hansı şəbəkə təhlükəsizliyinə aiddir?",
                "cavablar": ["A) Firewall", "B) Word processor", "C) File manager"],
                "dogru_cavab": "A) Firewall"
            },
            12: {
                "sual": "İnternet üzərindən fayl mübadiləsini təmin edən protokol hansıdır?",
                "cavablar": ["A) FTP", "B) HTTP", "C) HTTPS"],
                "dogru_cavab": "A) FTP"
            },
            13: {
                "sual": "Microsoft Excel-də hansı əməliyyat sistemi istifadə olunur?",
                "cavablar": ["A) Şəkil çəkmə", "B) Cədvəl yaratma", "C) Verilənlər bazası yaratma"],
                "dogru_cavab": "B) Cədvəl yaratma"
            },
            14: {
                "sual": "Kompüterin xarici yaddaşına nə daxildir?",
                "cavablar": ["A) CPU", "B) Monitor", "C) Hard disk"],
                "dogru_cavab": "C) Hard disk"
            },
            15: {
                "sual": "İnformatika elmi hansı sahələri əhatə edir?",
                "cavablar": ["A) Biologiya", "B) Məlumatların işlənməsi və saxlanması", "C) Kənd təsərrüfatı"],
                "dogru_cavab": "B) Məlumatların işlənməsi və saxlanması"
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
            if self.start.lower() == 'Q':
                print('\nSizinlə vaxt keçirmək çox xoş oldu  Sağolun!!!')
                sys.exit()

            elif self.secim.strip() == '' or self.start.isdigit():

                print("\nXahiş edirəm düzgün bir seçim daxil edin (boş və ya rəqəm olmamalıdır).")
            else:
                SualCavabOyunu()


ders = SualCavabOyunu()
