# 08.03/2024
# Primberdiyev Dilshod 
class SHaxs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
    def get_info(self):
        info=f"{self.ism} {self.familiya}. "    
        info+=f"pasport: {self.passport}, {self.tyil} yilda tug'ilgan "
        return info
    def get_age(self,yil):
        return f"{yil-self.tyil} yosh "
myself=SHaxs('Dilshod', "Primberdiyev", "AD001122",2005)
#print(myself.get_info())
class Talaba(SHaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism,familiya,passport,tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil
        self.fanlar=[]
    def get_idraqam(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich
    def get_info(self):
        info=f"{self.ism} {self.familiya} "
        info+=f"ID raqam: {self.idraqam} "
        return info
    def fanga_yozil(self):
        
        
class Manzil:
    def __init__(self,uy_nomer,kochasi,tuman,viloyat):
        self.uy_nomer=uy_nomer
        self.kochasi=kochasi
        self.tuman=tuman
        self.viloyat=viloyat
    def get_manzil(self):
        adres=f"{self.viloyat} viloyati, {self.tuman} tumani ,"
        adres+=f"{self.kochasi} ko'chasi. {self.uy_nomer}-uy"
        return adres
talaba1_manzil=Manzil(10, "Bo'stom", "Toshloq", "Farg'ona")
talaba1=Talaba("Dilshod","Primberdiyev","AD112233",2005,9988769,talaba1_manzil)
print(talaba1.manzil.get_manzil())
#Mohirdev Amaliyot 
class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
    def get_nom(self):
        return self.nomi
fan1=Fan("Matematika")
fan2=Fan("Fizika")
        
       
    
        
        
        
        
        
        
        
        
        
        
        
