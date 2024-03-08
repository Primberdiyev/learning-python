class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.universitet=""
    def get_ism(self):
        return self.ism
    def get_familiya(self):
        return self.familiya
    def get_yosh(self):
        return self.yosh
    def full_name(self):
        return f"{self.ism} {self.familiya}"
talaba1=Talaba("Dilshod","Primberdiyev",18)
talaba1.universitet="Tatu"
talaba2=Talaba("Valijon","SHomurodov",22)
class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi=fan_nomi
        self.talabalar=[]
        self.talabalar_soni=0
    def get_fan_nomi(self):
        return self.fan_nomi
    def get_talabalar(self):
        return [talaba.full_name() for talaba in self.talabalar]
      
    def get_talabalar_soni(self):
        return self.talabalar_soni
    def talaba_qosh(self,talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni+=1
matem=Fan("Algebra")
matem.talaba_qosh(talaba1)
matem.talaba_qosh(talaba2)

        
