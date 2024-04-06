mashinalar=['damas','lacetti','malibu']
mashinalar.insert(1,'nexia 2')
print(mashinalar)

#pop metodi
mashina=mashinalar.pop(1)
print(mashina)
print(mashinalar)
mashinalar.remove('damas')
print(mashinalar)

# clear metodi
mashinalar.clear()
print(mashinalar)


# sort va reverse metodlari
numbers=[32,34,45,-9,560]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# sorted metodi
sonlar=[23,43,54,-9,87]
sonlar2=sorted(sonlar)
print(sonlar2)

# noodatiy
royhat=[1]*4
print(royhat)

# royhatlarni qo'shish
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list1+list2
print(list3)

# massiv saralash
sonlar3=[0,1,2,3,4,5]
javob=sonlar3[:]
print(javob)
teskari=sonlar3[::-1]
print(teskari)
oraliq=sonlar3[::3]
print(oraliq)


# copy qilish
juft_sonlar=[0,2,4,6]
juft_sonlar_cpy=juft_sonlar[:]
juft_sonlar_cpy.append(8)
print(juft_sonlar)

# 2 ta ro'yhat bilan ishlash
toq_sonlar=[1,3,5,7,9]
toq_kvadrat=[i*i for i in toq_sonlar]
print(toq_sonlar)
print(toq_kvadrat)












