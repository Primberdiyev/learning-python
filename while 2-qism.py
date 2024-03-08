#1
ismlar=[]
n=1
while True:
    savol=f"{n}- do'stingiz ismini kiriting "
    ism=input(savol)
    ismlar.append(ism)
    takrorlash=input("davom etamizmi>>>")
    n+=1
    if(takrorlash!='ha'):
        break
print("sizni do'stingiz quyidagilar ")
for ism in ismlar:
    print(ism.title())
#2
ishora=True
n=1
dostlar={}
while ishora:
    savol=f"{n}-do'stingizni ismini kiriting>>>"
    ism=input(savol)
    yosh=input(f"{ism.title()} ning yoshini kiriting>>")
    dostlar[ism]=int(yosh)
    takrorlash=input("davom ettiramizmi>>>")
    n+=1
    if(takrorlash!='ha'):
        ishora=False
print("do'stlaringiz ismi va yoshi quyidagicha ")
for ism,yosh in dostlar.items():
    print(f"{ism} ning yoshi {yosh}")"""
#3 sikl yoramida ro'yhatdagi malumotlarni o'chirish
"""phones=['iphone','redmi','iphone','htc','samsung','iphone']
while 'iphone' in phones:
    phones.remove('iphone')
print(phones)
#3
t_soni=int(input("nechta talabani baholaymiz>>>"))
talabalar=[]
n=1
for talaba in range(t_soni):
    savol=f"{n}-talaba ismini kiriting>>>"
    talaba=input(savol)
    talabalar.append(talaba)
    n+=1

baholangan_talabalar={}
while talabalar:
    talaba=talabalar.pop()
    baho=input(f"{talaba} bahosini kiriting>>>")
    print(f"{talaba.title()} baholandi")
    baholangan_talabalar['talaba']=int(baho)
for ism,baho in baholangan_talabalar.items():
    print(f"{ism.title()}ning bahosi {baho}")
#4
n=int(input("nechta ovqat buyurtma qilmoqchisiz>>>"))
k=1
buyurtmalar=[]

for buyurtma in range(n):
    buyurtma=input(f"{k}-ovqatni kiriting>>>")
    buyurtmalar.append(buyurtma)
    k+=1
print(buyurtmalar)
#5
buyurtma=True 
k=1
buyurtmalar=[]
while buyurtma:
    buyurtma=input(f"{k}-ovqatni kiriting>>>")
    buyurtmalar.append(buyurtma)
    takrorlash=input("davom etamizmi>>>")
    k+=1
    if(takrorlash!='ha'):
        buyurtma=False
print(buyurtmalar)
mahsulotlar=[]
n=int(input("nechta mahsulot olmoqchisiz>>>"))
k=1
for mahsulot in range(n):
    mahsulot=input(f"{k}-mahsulot nomini kiriting>>>")
    mahsulotlar.append(mahsulot)
    k+=1
baho_mahsulotlar={}
while mahsulotlar:
    mahsulot=mahsulotlar.pop()
    narh=input(f"{mahsulot} narhini kiriting")
    baho_mahsulotlar[mahsulot]=int(narh)
for mahs,baho in baho_mahsulotlar.items():
    print(f"{mahs} ning narhi {baho}")
