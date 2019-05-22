a=int(input("select the starting meter   "))
b=int(input("enter your  ending meter   "))
print("1.auto,2.car,3.cab,4.bmw")
d=int(input("enter your name"))
c=a-b
if(a>=0):
   if(d==1):
     c=c*8
   elif(d==2):
     c=c*10
   elif(d==3):
     c=c*11
   elif(d==4):
      c=c*12
   else:
      print("enter the option")
   print("total meter" +str(a)+"km  to  "+str(b)+"km ")
   print("total amount is:  "+str(c)+"rs")
else:
  print("enter the correct Km")
