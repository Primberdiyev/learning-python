from turtle import *   
import turtle as turt  
  
tr = turt.Turtle()  
  
# Total No. of sides of the polygon to be drawn  
tomon= int(input("ko'pburchak necha tomonli bo'lsin "))  
  
# Total Length of each side of the polygon to be drawn  
olcham = int(input("Ko'pburchakning har bir tomonining uzunligi quyidagicha bo'lishi kerak: "))  
  
for j in range(tomon):  
  tr.forward(olcham)  
  tr.right(360/tomon)  