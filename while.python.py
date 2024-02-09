# 09.02.2024
# Primberiyev Dilshod
#while mavzusi
#1
"""a=int(input("a="))
b=int(input("b="))
while(a>=b):
    a-=b
print(a)"""
#2
"""son=1
while(son<=7):
    print(son)
    son=son+1
print("dastur tugadi")"""
#3
"""son=1
a=int(input("son kiriting>>>"))
while(son<=a):
    print(son,end=' ')
    son+=1
print("dastur tugadi")"""
#4
"""savol="istalgan son kiriting "
savol+="(dasturni to'xtatish uchun esa 'exit' so'zini kiriting)>>>"
qiymat=''
while(qiymat!='exit'):
    qiymat=input(savol)
    if(qiymat!='exit'):
        print(float(qiymat)**2)
print("dastur tugadi!!!")"""
#5
"""savol="istalgan son kiriting "
savol+="(dasturni to'xtatish uchun 'stop' so'zini kiriting)>>>"
qiymat=True
while(qiymat):
    qiymat=input(savol)
    if(qiymat=='stop'):
        qiymat=False
    else:
        print(float(qiymat)**2)
print("dastur tugadi !!!")"""
#6
savol="istalgan son kiriting"
savol+="(dasturni to'xtatmoqchi bo'lsangiz 'stop' so'zini kiriting)  "
qiymat=True
while(qiymat):
    qiymat=input(savol)
    if(qiymat=='stop'):
        qiymat=False
    else:
        print(float(qiymat)**3)
print("dastur tugadi ")
#7 
savol="istalgan son kiriting "
savol+="(dasturni to'xtatishni istasangiz 'stop' so'zini kiriting) "
qiymat=''
while True:    #abadiy sikl
    qiymat=input(savol)
    if(qiymat=='stop'):
        break
    else:
        print(float(qiymat)**2)
print("dastur tugadi!!!")
#8
sonlar=list(range(1,11))
for son in sonlar:
    if(son==5):
        break
    print(float(son)**2)
    #9

for son in range(1,12):
    if(son==5):
        continue
    else:
        print(f"{son} kvadrati {(son)**2} ga teng")
#10
son=0
while(son<=12):
    son+=1
    if(son%2==0):
        continue
    else:
        print(son)
#11
num=0
while(num<=12):
    num+=1
    if(num%2!=0):
        continue
    else:
        print(num)
#mohirdev amaliyot
#1
savol="yoqtirgan kitibingiz nomini kiriting  "
javob=True
while(javob):
    javob=input(savol)
    if(javob=='stop'):
        break
print("dastur tugadi")
#2
savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): " 

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue
    
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("dastur tugadi")

       

    
    
        
   
    
    
    
    
    



    

    