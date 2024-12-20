# data = 'Mell-Gibson-Hoffman'
# """
# name: Mell
# surname: Gibson
# fullname Mell Gibson Hoffman
# """
#
#
# new = data.split('-')
# print(new)
# # new_ =' '.join(new)
# # print(new_)
# # print(f"name : {new_[:5]}\nsurname:{new_[5:11]}\nfullname: {new_}")
#
#
# sozluk = {'name': new[0],'surname': new[1], 'fulname': ' '.join(new)}
#
# for k,v in sozluk.items():
#     print(f"{k} {v}")
#
#


import os
import shutil

def uzanti_tap():
    uzanti = r'C:\Users\user\PycharmProjects\ders1_19.11.2024\test\test_1\style.css'

    print(os.path.splitext(uzanti)[1].replace('.',''))
    print(os.path.splitext(uzanti)[1].lstrip('.'))


    elementler = os.listdir()

    # elem_in = [f"{index+1}. {i}" for index, i in enumerate(elementler)]
    # print(elem_in,sep='\n')


    for index,i  in enumerate(elementler):
        print(f"{index}.{i}")

uzanti_tap()

def fayl_sec():
    axtaris_fayli = r'C:\Users\user\PycharmProjects\ders1_19.11.2024\test'

    css_folder = os.path.join(axtaris_fayli,'css')
    html_folder = os.path.join(axtaris_fayli,'html')

    os.makedirs(css_folder,exist_ok=True)
    os.makedirs(html_folder,exist_ok=True)



    for root,dirs,fayl in os.walk(axtaris_fayli):
        for index,i in enumerate(fayl,start=1):
            print(f"{index}.{i}")


    for root,dirs,files in os.walk(axtaris_fayli):
        for file in files:
            file_path = os.path.join(root,file)
            #print(file_path)

        if file.endswith('css'):
            shutil.move(file_path,os.path.join(css_folder,file))

        elif file.endswith('html'):
            shutil.move(file_path,os.path.join(html_folder,file))

    print('Fayllar muaviq qovluqlara kocuruldu')


fayl_sec()
