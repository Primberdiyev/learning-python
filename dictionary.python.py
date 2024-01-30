#1
"""hobby={"sport":"boks","music":"tanovor","youtube":"subyektiv"}
print(hobby["sport"])
print(hobby["music"])
print(hobby["youtube"])
print(f"men odatda youtubeda {hobby['youtube']} kanalini kuzatib boraman")
hobby["serial"]="panjara ortida"
hobby["kino"]="chapaqay"
print(hobby)
#2
n=input("nechta meva olmoqchisz ")
n=int(n)
mevalar=[]
bor_mevalar={"olma":"10000","shaftoli":"3000","uzum":"5000","shakar":"4000","tuz":"2000"}
for k in range(n):
    mevalar.append(input(f"{k+1}-mevani kiriting "))

for meva in mevalar:
    if meva in bor_mevalar:
        print(f"{meva} bizda bor")
    else:
        print(f"bizda {meva} yo'q")
# bo'sh lug'at
malumot={}
malumot["ism"]=input("ismingizni kiriting ")
malumot["turar_joy"]=str(input("qayerda yashayapsiz "))
malumot["t_yil"]=int(input("nechanchi yili tug'ilgansiz "))
print(f"assalomu aleykum {malumot['ism']}, \
siz {malumot['turar_joy']} da tug'ilgansiz va \
siz {2024-malumot['t_yil']} yoshdasiz")
# lugatdan malum elementlarni olib tashlash
dasturlash={"til":"python","talim_shakli":"online","ustoz":"mohirdev"}
del dasturlash['talim_shakli']
print(dasturlash)
dasturlash2={}
dasturlash2["til"]=input("qaysi dasturlash tilini o'rganyapsiz ")
dasturlash2["talim_shakli"]=input("online o'rganyapsizmi yoki offline ")
dasturlash2["ustoz"]=input("ustozingiz kim ")
print(dasturlash2)
del dasturlash2["talim_shakli"]
print("farqni ko'ring \n",dasturlash2)
en_uz={
       "lower":"kamaytirmoq",
       "expenditure":"xarajatlarim",
       "nice": "yahshi",
       "worse":'yomonroq',
       "developer":"dasturchi"
       
       
       }
print(en_uz)
print(en_uz['lower'])
del en_uz['nice']
print(en_uz)
bad=en_uz.get('worse',"think again")
print(bad)
print(en_uz)
# mohirdevdagi amaliyot 
dadam={"ism":"Eldor Xudoyberdiyev","t_yil":"1976","kasb":"quruvchi"}
print(f"mening dadamni ismi {dadam['ism']}, u {dadam['t_yil']} da tug'ilgan, \
      uning kasbi {dadam['kasb']}")
onam={}
onam['ism']="Gulziyo Xudoyberdiyeva"
onam["kasb"]="dasturchining onasi"
onam["t_yil"]=1979
print(f"mening  onam {onam['ism']}, u {onam['t_yil']} da tug'ilganlar,\
ularning kasbi {onam['kasb']}")
sevimli_taom={
    "dadam":"osh",
    "onam":"shashlik",
    "saida": "katorshka",
    "sayyora":"garux",
    "Developerbek":"bosma"
    
    }

print(f"dadamning sevimli taomi {sevimli_taom['dadam']}")
print(f"onajonimning sevimli taomi {sevimli_taom['onam']}")
print(f"o'zimning sevimli taomim {sevimli_taom['Developerbek']}")"""
skills={
        "int":"butun sonlar tipi",
        "float":"xaqiqiy sonlar tipi",
        "string":"matnli tip",
        "del":"ochirish aperatori",
        "remove":"ochirish operatori",
        "insert":"joylash uchun kerakli",
        "title":"birinchi harfni katta qilib beradi ",
        "upper":"barcha harflarini katta qilib beradi",
        "lower":"barcha harflarini kichik qiib beradi ",
        "get":"olish uchun ishlatiladi",
        "type":"tipini aniqlovchi metod",
        
       }
yangi_soz=input("qidirmoqchi bo'lgan so'zingizni kiriting ")
print(skills.get(yangi_soz,"bunday so'z mavjud emas "))





















