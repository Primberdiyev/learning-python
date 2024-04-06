class Talaba:
    def __init__(self,ism,yosh,kursi,talim_shakli):
        self.ism=ism
        self.yosh=yosh
        self.talim_shakli=talim_shakli
        self.kursi=kursi
    def get_ism(self):
        return self.ism.title()
    def get_yosh(self):
        return self.yosh
    def get_kursi(self):
        return self.kursi
    def set_kursi(self,kurs):
       # if kurs>=0:
        self.kursi=kurs
       # else:
           # raise ("kurs manfiy bo'ishi mumkun emas")
        return self.kursi
    def gett_talim_shakli(self):
        return self.get_talim_shakli.title()
talaba1=Talaba("dilshod",10,1,"kunduzgi")
print(talaba1.get_ism())