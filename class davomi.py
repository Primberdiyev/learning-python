"""from uuid import uuid4
class Avto:
    __obyektlar_soni=0
    Avtomabil haqida klass
    def __init__(self,model,rang,yil,km):
        self.model=model
        self.rang=rang
        self.yil=yil
        self.__km=km
        self.__id_raqam=uuid4()
        Avto.__obyektlar_soni+=1
    @classmethod
    def get_obyektlar_soni(cls):
        return Avto.__obyektlar_soni
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id_raqam
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            print("avtomabil yurgan masofasini kamaytirib bo'lmaydi")
        
avto1=Avto("Lacetti","qora",2021,1000)
print(avto1.get_obyektlar_soni())"""
class Inson:
    """inson haqida klass"""
    __obyekt_soni=0
    def __init__(self,ism,familiya,jinsi):
        self.ism=ism
        self.familiya=familiya
        self.__jinsi=jinsi
class Talaba(Inson):
    def __init__(self,ism,familiya,jinsi,manzil):
        super().__init__(ism, familiya, jinsi)
        self.manzil=manzil
    def get_jinsi(self):
            return self.__jinsi
        
talaba1=Talaba("Dilshod","Primberdiyev","Erkak","Farg'ona viloyati")
    
        

