#Dilshod Primberdiyev
#06.02.2024
"""malibus=[]
for n in range(10):
    new_car={
        "model":"malibu",
        "km":0,
        "rang":None,
        "karobka":"avto",
        "narh":None
         }
    malibus.append(new_car)
print(malibus)
for malibu in malibus[:3]:
    malibu['rang']="qora"
for malibu in malibus[3:6]:
    malibu['rang']="qizil"
for malibu in malibus[6:]:
    malibu['rang']="oq"
for malibu in malibus:
    print(malibu)
for malibu in malibus[6:]:
    malibu['karobka']="mexanika"
for malibu in malibus:
    if(malibu['karobka']=='avto'):
        malibu['narh']=40000
    else:
        malibu['narh']=35000
for malibu in malibus:
    print(malibu)"""
coders={
        "Dilshod":['c++',"python"],
        "Doniyor":['c++',"c#"],
        "Ali":["php","sql"],
        "vali":['php',"leravel"]        
        
        }
"""for ism,tillar in coders.items():
    print(f"{ism.title()} quyidagicha tillarni biladi")
    for til in tillar:
        print(til.upper())"""
for ism,tillar in coders.items():
    print(f"{ism.title()} quyidagicha tillarni biladi")
    for til in tillar:
        print(til.upper())
#Mohirdev amaliyot 
buyuk0={
    'ism':"steve Jobs",
    "t_yil":1955,
    "t_joy":"kaliforniya",
    "umr":55
    }
buyuk1={
    "ism":"Bill Gates",
    "t_yil":1955,
    "t_joy":"vashington",
    "umr":65
    
    }
buyuk2={
        "shahar":"toshkent"
        
    "ism":"islom karimov",
    "t_yil":1938,
    "t_joy":"samarqand",
    "umr":78
    
    }
buyuklar=[buyuk0,buyuk1,buyuk2]
for buyuk in buyuklar:
    print(f"{buyuk['ism'].title()} {buyuk['t_yil']}-yilda {buyuk['t_joy'].title()}da tug'ilgan "
          f"va u {buyuk['umr']} yil umr ko'rgan\n")
buyuk0["loyihalar"]=["apple","va yana bir necha "]
buyuk1["loyihalar"]=["Microsoft",'Ofis']
buyuk2['loyihalar']=['besh tashabbus',"va yana bir nechta"]
for buyuk in buyuklar:
    print(f"{buyuk['ism'].title()} quyidagicha ishlarni amalga oshirgan")
    for loyiha in buyuk['loyihalar']:
        print(loyiha.title())
kinolar={
    "ali":["abdullajon",'novda'],
    "vali":['jumong',"panjara ortida"],
    "Dilshod":["polat alemdar",'chapaqay']    
    
    }
for ism,cinolar in kinolar.items():
    print(f"{ism.title()} quyidagicha kinolarni yahshi ko'radi")
    for cino in cinolar:
        print(cino.title())