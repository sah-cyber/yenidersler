import random
import time
def zerler_():
    count = 0
    while True:
        count += 1
        print(f"saygac {count}")
        zer_1 = random.randint(1,6)
        print(f'birinci zer deyeri {zer_1}')
        zer_2 = random.randint(1,6)
        print(f'ikinci zerin deyeri {zer_2}')
        if zer_1 ==6 and zer_2 ==6:
            print(f"zerin ilk defeye 6 qowa duwmesi ucun zerler {count} atildi")
            break
zerler_()



def ilk_6(atis_sayi):
    zerler = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    count = 0
    found = False
    start_time = time.time()

    for i in range(atis_sayi):
        say = random.randint(1, 6)
        zerler[say] += 1




        if zerler[6] == 6 and not found:
            count += 1
            end_time = time.time()-start_time
            print('ilk defe 6 qowa {} defeye geldi'.format(count))
            print('zer atislari {}'.format(zerler))
            print(end_time)
            found = True

    print('son veziyyet {}'.format(zerler))


ilk_6(atis_sayi=int(input('Atis sayini verin: ')))

