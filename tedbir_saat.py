

def tedbir_zaman():

    import pytz
    from datetime import datetime
    print('Salam Tedbirini baslanma vaxti Baki vaxti ile 25.12.2024-cu il saat 18:45 dedir.')
    seherler = input('Zehmet olmasa yasadiginiz seheri qeyd edin: ').strip().lower()

    london = pytz.timezone('Europe/London')
    tokio = pytz.timezone('Asia/Tokyo')
    newyork = pytz.timezone('America/New_york')
    turkiye = pytz.timezone('Europe/Istanbul')
    baki = pytz.timezone('Asia/Baku')

    baki_time = datetime(2024,12,25,18,45,0,tzinfo=baki)

    if seherler.isalpha() and seherler != '':


        if seherler == 'london':
            london_time = baki_time.astimezone(london)
            print(f"Tedbir London zamani ile {london_time.strftime('%Y-%m-%d %H:%M:%S')}")

        elif seherler == 'tokio':
            tokio_time = baki_time.astimezone(tokio)
            print(f"Tedbir Tokio zamani ile {tokio_time.strftime('%Y-%m-%d %H:%M:%S')}")

        elif seherler == 'newyork':
            newyork_time = baki_time.astimezone(newyork)
            print(f"Tedbir Newyork zamani ile {newyork_time.strftime('%Y-%m-%d %H:%M:%S')}")

        elif seherler== 'turkiye':
            turkiye_time = baki_time.astimezone(turkiye)
            print(f"Tedbir Turkiye zamani ile {turkiye_time.strftime('%Y-%m-%d %H:%M:%S')}")

        elif seherler == 'baki':
            baki_time = baki_time.astimezone(baki)
            print(f"Tedbir Baki zamani ile {baki_time.strftime('%Y-%m-%d %H:%M:%S')}")

        else:
            print('Bu sherin qeydiyati baslamayib')
    else:
        print("Seherin adini duzgun qeyd edin")


tedbir_zaman()


