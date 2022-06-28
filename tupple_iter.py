mytuple = ("apple", "banana", "cherry") #tuple

myit = iter(mytuple)    #using iter method
print(myit)  #format
print(next(myit))#appple
print(next(myit))  #banana
print(next(myit))  #cherry

#using iterator in loops. 

#for loop creates an iterator object and executes the
 #next() method for each loop.
for i in mytuple:
    print(i)
