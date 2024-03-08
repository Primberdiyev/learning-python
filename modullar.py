def car_info(model,rang,yil,karobka,narh):
    """foydalanuvchidan ma'lumot qabul qilib ro'yhat qaytaruvchi funksiya"""
    info={
        "model":model,
        "rang":rang,
        "yil":yil,
        "karobka":karobka,
        "narh":narh
        }
    return info

def kirit():
    """lugatlarni royhatga joylovchi funksiya"""
    avtolar=[]
    while True:
        model=input("mashina madelini kiriting ")
        rang=input("mashina rangini kiriting ")
        yil=input("mashina yilini kiriting ")
        karobka=input("karobka: ")
        narh=input("narh: ")
        avtolar.append(car_info(model,rang,yil,karobka,narh))
        takror=input("yana davom ettirasizmi (yes/no)")
        if takror=='no':
            break
    return avtolar
def chiqar(car_info):
    print(f"{car_info['rang'].title()} {car_info['model']}, "
          f"karobkasi-{car_info['karobka'].title()}, narhi - {car_info['narh']}$")
   
    
    
    
