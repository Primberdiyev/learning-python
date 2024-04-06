# #tupe ko'rinishi
#mytuple=['olma','o\'rik','gilos','shaftoli']
# print(mytuple)


#tuple elementlariga murojaat qilish
# print(mytuple[0])
# print(f"mening eng sevimli mevam {mytuple[2]}")
# print(mytuple[-2])


# # tuple va dict farqlari
# mydict=['sen','eng','zo\'r','dasturchisan']
# mydict[0]='Dilshod'
# print(mydict)
# # output ['Dilshod', 'eng', "zo'r", 'dasturchisan']

# mytuple=('Dilshod','eng','zor','dasturchisan')
# mytuple[0]='sen'
# print(mytuple)
# # output TypeError:
    
    
## tuple elementlari sonini bilish
# mytuple=('lacetti','Damas','Tiko')
# print(len(mytuple))


# #tuple elementalri orasida bitta element bir nechta kelganda uning nech marta kelganini 
# #                                                                        bilish
# myletter=('d','e','v','e','l','o','p','e','r')
# print(myletter.count('e'))


# # tuple da ma'lum elementning indeksiga murojaat qilish
# tuples=['hi','strong','developer']
# print(tuples.index('strong'))

# # tuple dan list ga o'tish
# sciences=('math','physics','chemistry')
# sciences_list=list(sciences)
# print(sciences_list)

# # tuple elementlari bilan ishash
# a=(9,8,7,6,5,4,3,2,1)
# print(a[::-1])
# print(a[3:5])
# print(a[1:2])

# my_tuple=('hi','you','will','be','developer')
# a,b,c,d,e=my_tuple
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# my_tuple=('hi','you','are','strong','developer')
# a,*b,c=my_tuple
# print(a)
# print(c)
# print(*b)
      
# import sys
# tuple_1=(1,2,3,4,5,6,'salom')
# tuple_2=[1,2,3,4,5,6,'salom']
# print("size of tuple1",sys.getsizeof(tuple_1),'bytes')
# print("size of tuple1",sys.getsizeof(tuple_2),'bytes')


# # berilgan tuple ichidagi sonlarni o'sish tartibida chiqarish
# tuple_number=(1,34,32,21,23,5)
# tuple_number=list(tuple_number)
# tuple_number=sorted(tuple_number)


# # print(tuple_number)

# numbers=[1,2,3,4,54,6]
# mx=max(numbers)
# mn=min(numbers)


# list1=(2,5,9)
# ans=[(val,pow(val,3)) for val in list1]
# print(ans)


# list1=[1,4,8]
# list2=list(map(lambda x:(x,x**3), list1))
# print(list2)

# tuple elementlarini yig'indisini hisoblovchi funksiya
# def summation(tuples):
#     tuples=list(tuples)
#     ans=sum(tuples)
#     return ans
# tuples1=(1,2,3,4,5,6,7,8,9)
# tuples2=(10,11,12,13,14,15)
# tuples3=tuples1+tuples2
# print(summation(tuples1))
# print(summation(tuples2))
# print(summation(tuples3))


# 2 ta tuple tipida sonlar berilgan ushbu tuplelardan birini ikkinchisiga qoldiqli bo'lgandagi
# yangi tuple  no ekranga chiqaring
# tuple1=(2,3,4,5,100)
# tuple2=(7,8,9,10,10)
# print(f"first tuple is {tuple1}")
# print(f"second tuple is {tuple2}")
# tuple1=list(tuple1)
# tuple2=list(tuple2)
# tuple3=[]
# for i in range(len(tuple1)):
#     tuple3.append(tuple1[i]%tuple2[i])
# tuple3=tuple(tuple3)
# print(f"the answer is {tuple3}")
    

# tuple1=(1,2,3,4,5,634)
# tuple2=(3,4,2,12,5,6)
# res=[ele1%ele2 for ele1,ele2 in zip(tuple1,tuple2)]
# print(res)    
    
tuple1=(1, 5, 7, 8, 10)
tuple2=[tuple1[i]*tuple1[i+1] for i in range(len(tuple1)-1)]
tuple2=tuple(tuple2)
print(tuple2)

    
    
    
    
    
    
    






