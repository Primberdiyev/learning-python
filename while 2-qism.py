#10
#Primberdiyev Dilshod
#while ro'yhatlar va lug'atlar
#1
ismlar=[]
n=1
while True:
    savol="{n}- do'stingiz ismini kiriting "
    ism=input(savol)
    ismlar.append(ism)
    takrorlash=input("davom etamizmi>>>")
    if(takrorlash!='ha'):
        break
print("sizni do'stingiz quyidagilar ")
for ism in ismlar:
    print(ism.title())
