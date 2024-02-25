def malumotlar(ism,familiya,t_joy,t_yil,t_raqam=None):
    information={
        "ism":ism,
        "familiya":familiya,
        "t_joy":t_joy,
        "t_yil":t_yil,
        "yosh":2024-t_yil,
        't_raqam':t_raqam
        }
   
 #   """foydalanuvchi haqida to'liq ma'lumot"""
    information={
        "ism":ism,
        "familiya":familiya,
        't_joy':t_joy,
        "t_yil":t_yil,
        't_raqam':t_raqam,
        "yosh":2024-int(t_yil)
        }
    return information
person1=malumotlar("Dilshod", "Primberdiyev", "Bo'ston", 2005,902778631)
person2=malumotlar("Humoyun","Begmatov","Polsha",2005)
persons=[person1,person2]

person3=malumotlar('Ali', 'Valiyev', 'oltiariq', 2012)
person4=malumotlar("Hasan","Husanov","beshkapa",2004,904543324)
persons.append(person3)
persons.append(person4)
while persons:
    person=persons.pop()
    if(person['t_raqam']):
        raqam=person['t_raqam']
    else:
        raqam="nomalum"
    print(f"{person['ism']} {person['familiya']} {person['t_joy']} da tug'ilgan."
          f"uning yoshi {person['yosh']}. uning telefon raqami {raqam}")
#3
def katt_aniqla (x,y,z):
   """3 ta son qabul qiib kattasini qaytaruvchi funksiya"""
    numbers=[x,y,z]
    min,max=x,y
    for number in numbers:
        if min>number:
            min=number
        if max<number:
            max=number
   
    return max,min
print(katt_aniqla(3, 54, -5))
#4
def new_ex(r):
   # """function that asks the user for the radius
    of a circle and returns the diameter of its face
    informations={
        "surface":3.14*r*r,
        "radius":r,
        "diameter":2*r
        }
    return informations
print(new_ex(2))
#5
def find_prime(x):
    """you can use this function to determine a prime number"""
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            c+=1
    if(c==2):
        print(f"{x} soni tub son")
    else:
        print(f"bu {x} soni tub emas")
find_prime(43)
find_prime(34)
find_prime(2)



def find_prime(a,b):
    prime_numbers=[]
    for i in range(a,b+1):
        tub=True
        if i==1:
            tub=False
        elif i==2:
            tub=True
        else:
            for n in range(2,i):
                if i%n==0:
                    tub=False
                    break
    return prime_numbers
def give_grade(names):
    grades={}
    while names:
        name=names.pop()
        grade=input(f"enter {name.title()}'s grade ")
        grades[name]=int(grade)
    return grades
names1=['olim','vali','qobil']
print(give_grade(names1[:]))
print(names1)
def katta_harf(sozlar):
    for i in range(len(sozlar)):
        sozlar[i]=sozlar[i].title()
ismlar=['men','eng','zo\'r', 'dasturchiman']
katta_harf(ismlar[:])
print(ismlar)
    
    
    
    
    
    
