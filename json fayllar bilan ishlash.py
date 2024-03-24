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
 

bemor={
       "ism":"Alijon",
       "yosh":18,
       "allergiya":None,
       "oila":True,
       "dorilar": [{'nomi':"Sproks",'miqdori':125},{'nomi':"Parastamol","miqdori":120}]
      }
bemor_json=json.dumps(bemor,indent=4)
with open('bemor_json','w') as f:
    json.dump(bemor_json,f)
with open('bemor_py','w') as file:
    json.dump(bemor,file)
fact="Dilshod Primberdiyev eng zo'r dasturchi"
fact_json=json.dumps(fact)
fact_py=json.loads(fact_json)
with open('bemor_py') as file:
    fayl=json.load(file)
print(fayl)       
       