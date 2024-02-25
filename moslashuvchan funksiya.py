# Primberdiyev Dilshod
# 25.02.2024
# moslashuvchan funksiya
#1
"""def summa(*sonlar):
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi
print(summa(1,2,3,4,))
print(summa(1,2))
def summa(*sonlar):
    return sum(sonlar)
print(summa(1,2,3,4,))
print(summa(1,2))

def summa1(x,y,*sonlar):
    return x+y+sum(sonlar)
print(summa1(1,2,4))"""
#2
"""def avto_info(model,yil,**qoshimcha):
    qoshimcha['model']=model
    qoshimcha['yil']=yil
    return qoshimcha
avto1=avto_info("adidas",2019,rang="qora",karobka="avto")
print(avto1)"""
#3
"""def kopaytma(*sonlar):
    c=1
    for son in sonlar:
        c*=son
    return c
print(kopaytma(2,3,4,5))"""
#4
def info_student(name,age,**addition):
    addition['name']=name
    addition['age']=age
    return addition
print(info_student("Dilshod",18,sport="Boks"))
        
    