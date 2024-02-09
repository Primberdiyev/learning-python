"""talaba={
        "yosh":"18",
        "ism":"Dilshod",
        "kasb":"dasturchi",
        "universitet":"tatu",
        "fakultet":"Kif",
        "kurs":4
        }
#print(talaba['yosh'])
#yangi metod items() metodi
#print(talaba.items())
#for k,v in talaba.items():
 #   print(f"{k} - {v}")
#for keys, values in talaba.items():
 #   print(f"kalit - {keys}")
 #  print(f"qiymat - {values}\n")
telefonlar={
    "ali":"nokia",
    "vali":"redmi",
    "nozim":"iphone",
    "kozim":"HTC",
    "mardon":"smart 7 +",
    "sardor":"redmi"
    
    }

for k ,v in telefonlar.items():
    if k.lower()=="kozim":
        print(f"{k.title()} ning telefoni {v.upper()}")
    else:
        print(f"{k.title()}ning telefoni  {v.title()}")
mahsulotlar_narxi={
    "olma":1200,
    "uzum":10000,
    "olcha":5000,
    "banan":20000
    }"""
"""print("bizda bor mahsulotlar")
for mahsulot in mahsulotlar_narxi:
    print(mahsulot.title())"""
"""bozorlik={"olma","anjir","shaftoli","banan"}
for mahsulot2 in mahsulotlar_narxi:
    if mahsulot2 in bozorlik:
        print(f"{mahsulot2} narxi {mahsulotlar_narxi[mahsulot2]}")
    else:
        print(f"kechirasiz bizda {mahsulot2.title()} yo'q")
qoshiqlar={
    "mendirman_osha":"Ozodbek nazarbekov",
    "ota ona":"shoxrux",
    "ketgim kelmayapti":"oxunjon madaliyev",
    "qishlog'im":"mahmud nomozov"
    }
kerakli_qoshiqlar=[]
kerakli_qoshiqlar.append(input("yoqtirgan qo'shig'ingizni nomini yozib bering \
 men sizga uning muallifini topib beraman>>>>"))
for qoshiq in kerakli_qoshiqlar:
     if qoshiq in qoshiqlar:
         print(f"{qoshiq} musiqasining muallifi {qoshiqlar[qoshiq]}")
     else:
        print("kechirasiz, bizda bu haqida hech qanday malumot yo'q")
for tel in telefonlar.values():
    print(f"bizda {tel} bor\n")
for tel2 in set(telefonlar.values()):
    print(f"bizda {tel2} bor")"""
#mohirdev amaliyot
#1
izohli_lugat={
    "int":"butun sonlar tipi",
    "float":"haqiqiy sonlar tipi",
    "keys":"lug'atdagi kalit so'z",
    "values":"lug'atdagi qiymat",
    "items":"lug;atdagi elementlar",
    "upper":"string toifasidagi matnlarni harfini katta qilib beradi",
    "title":"string toifasidagi bosh harfini kichik qilib beradi",
    "lower":"string toifasidagi matnlarni harfini kichik qilib beradi ",
    "type":"o'zgaruvchini tipini aniqlab beradi",
    "set":"qiymatlarni saralab beradi"
    
    }
for k,v in sorted(izohli_lugat.items()):
    print(f"{k} - {v}")
#2
davlat_poytaxt={
    "uzbekistan":"toshkent",
    "rossiya":"moskva",
    "yaponiya":"tokyo",
    "fransiya":"parij",
    "germaniya":"berlin",
    "turkiya":"istambul",
    "meksika":"meksika"
    }
print("dunyo davlatlari ")
for davlat in sorted(davlat_poytaxt.keys()):
    print(davlat.title())
print("dunyo davlatlarining poytaxti")
for poytaxt in sorted(davlat_poytaxt.values()):
    print(poytaxt.title())
#3
davlat1=input("qaysi davlat poytaxtini bilishni hohlaysiz>>>")

    
#4
menu={
      "osh":2000,
      "shorva":15000,
      "salat":2000,
      "choy":2000,
      "kofee":1000,
      "hotdog":1200,
      "somsa":4000,
      "perjka":500,
      "lavash":15000
     }
buyurtmalar=[]
buyurtmalar.append(input("birinchi ovqatni kiriting>>>"))
buyurtmalar.append(input("ikkinchi ovqatni kiriting>>>"))
buyurtmalar.append(input("uchinchi ovqatni kiriting>>>"))
for buyurtma in buyurtmalar:
    if buyurtma in menu.keys():
        print(f"{buyurtma.title()} narxi {menu[buyurtma]}")
    else:
        print(f"kechirasiz, bizda {buyurtma.title()} yo'q")




