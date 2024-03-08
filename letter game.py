import random as r
from uzwords import words
def soz_tanla():
    soz=r.choice(words)
    while ' ' in soz or "_" in soz:
        soz=r.choice(words)
    return soz
def tekshir(kiritilgan_harf,soz):
    umumiy=""
    for harf in soz:
        if harf in kiritilgan_harf:
            umumiy+=harf
        else:
            umumiy+="-"
    return umumiy
def boshla():
    soz=soz_tanla()
    soz=soz.lower()
    kerakli_harf=set(soz)
    kiritilgan_harflar=""
    print(f"men  {len(soz)} xonali so'z o'yladim, topa olasizmi ")
    while len(kerakli_harf)>0:
        print(tekshir(kiritilgan_harflar,soz))
        harf=input("harf kiriting ")
        harf=harf.lower()
        if harf in kiritilgan_harflar:
            print("bu harfni avval kiritgansiz ")
        elif harf in soz:
            print(f"bu {harf} harfi to'g'ri ")
            kerakli_harf.remove(harf)
        else:
            print("bu harf so'z tarkibida mavjud emas ")
        kiritilgan_harflar+=harf
    print(f"tabrilayman {soz} so'zini to'g'ri topdingiz fh")