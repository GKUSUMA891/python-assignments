mystr = "banana"    #string
myit = iter(mystr)  #using iter method

print(next(myit))    #b
print(next(myit))   #a
print(next(myit))    #n
print(next(myit))     #a
print(next(myit))     #n
print(next(myit))     #a

for i in mystr:
    print("iteration:",i)
