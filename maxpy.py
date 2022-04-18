
#first way
def maximum_nbr(givenlist):
    maxi=max(givenlist)
    return givenlist
givenlist=[100,2334,567,345,89,10]
print(max(givenlist))
print(maximum_nbr(givenlist))
#second way
num1=int(input("enter first value :"))
num2=int(input("enter second value :"))
if(num1>num2):
 print("num1 is maximum")
else:
 print("num2 is maximum")
#third way
a=200
b=399
if(a>b):
   print("a=200 is maximmum",a)
elif(a<b):
 print("b=399 is maximum",b)
else:
 print("a and b are equal") 
