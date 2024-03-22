import json 

x=10
x_json=json.dumps(x)
y=2.3
y_json=json.dumps(y)
#print(type(y_json))
#demak biz json faylga o'tkazish uchun json kutubxonasini chaqirishimiz kerak
# va dumps() metodidan foydalanishimiz kerak, json faylidagi malumotlar odatda string toifasida bo'ladi


# yana bir narsani aytib o'tish kerakki elementlarni json formatga o'tkazganda u huddi javascript tilidagi malunmot 
#turi kabi o'tadi , quyidagi misol orqali ko'rib olishingiz mumkun
m=True
m_json=json.dumps(m)
#print(m_json)
sonlar=(1,23,4,56,756)
sonlar2=json.dumps(sonlar)
 
