"""yosh=input("yoshingizni kiriting ")
yosh=int(yosh)
print(f"siz {2024-yosh}-yilda tug'ilgansiz")"""



"""yosh=input("yoshingizni kiriting ")
try:
    yosh=int(yosh)
    print(f"siz {2024-yosh}-yilda tug'ilgansiz ")
except:
    print(f"siz {2024-yosh}-yilda tug'ilgansiz ")"""
    
    
    
"""baho=input("Dasturlashdan nechchi baho oldingiz ")
try:
    baho=int(baho)
except:
    print("iltimos bahoni butun sonlarda kiriting")
else:
    print(f"sizning bahoyingiz {baho} ga teng")"""
    
    
"""fail_num=input("1-semestrda nechta fandan qaytaga qoldingiz ")
try:
    fail_num=int(fail_num)
except:
    print("siz butun son kiritmadingiz ")
else:
    print(f"xa demak siz {fail_num} ta fandan yiqilibsiz")"""
    
    
    
    
"""user={
      "name":"Dilshodbek",
      "age":19,
      "email":"Dilshoddeveloper2005@gmail.com",
      "phone":998902778631
      }
key="phones"
try:
    print(f"{user[key]}")
except  KeyError:
    print("bunday kalit mavjud emas")"""
    
    
"""filename="information" # bunday file komputerimda yo'q
try:
    with open(filename) as file:
        a=file.read()
except FileNotFoundError:
    print(f"{filename} file mavjud emas")
else:
    print(a)"""


while True:
    num=input("1-semestrda nechta fandan qaytaga qoldingiz ")
    if num.isdigit():
        print(f"xa,demak siz {num} ta fandan yiqilgan ekansiz")
        break;
        
    
    
    
    
     
      
      





