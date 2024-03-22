#dubder metodlar 
class Avto:
    """avtomabil haqida klass"""
    __obyekt_soni=0
    def __init__(self,rang,model,yil,narh):
        self.rang=rang
        self.model=model
    
        self.yil=yil
        self.narh=narh
        Avto.__obyekt_soni+=1
    def __repr__(self):
        return f"{self.rang} {self.model}"
    def __lt__(self,y):
        return self.narh<y.narh
    def __le__(self,k):
        return self.narh<=k.narh
    def __eq__(self,q):
        return self.narh==q.narh
class Avtosalon:
    """avtosalonlar haqida klasslar"""
    def __init__(self,name):
        self.name=name
        self.msoni=[]
    def __repr__(self):
        return f"{self.name} avtosaloni "
    def __getitem__(self,index):
        return self.msoni[index]
    def __call__(self):
        return [avto for avto in self.msoni]

    def add_car(self,*name):
        for car in name:
            if isinstance(car, Avto):
                self.msoni.append(car)
            else:
                print("Avto klassiga oid mashina kiring")


avto1=Avto("qora","lacetti",2021,6000)
avto2=Avto("oq","damas",2007,4000)
salon1=Avtosalon("arzon")
salon1.add_car(avto1,avto2)
salon2=Avtosalon("qimmat")
salon2.add_car(avto1)






import math

n=int(input())
a=[]
for i in range(1,n+1):
    k=int(input())
    a.append(k)
mn=a[0]
mx=0
for i in range(len(a)):
    if a[i]<mn:
        mn=a[i]
    if a[i]>mx:
        mx=a[i]
print(mx,math.floor(mx),mn)
    
# Eng katta 3 ta sonni topish
a.sort(reverse=True)
eng_katta_3_tasini_qaytaruvchi = a[:3]

print("Eng katta 3 ta son:", eng_katta_3_tasini_qaytaruvchi)


        
        
        
        
        
        
    