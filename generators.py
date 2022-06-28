def my_class():
    yield 1
    yield 2
    yield 'a'
    yield 'b'
    yield 3
friend=my_class()
print(friend)     #format
#print(next(friend)) #1
#print(next(friend))        #2
#print(next(friend))        #a
#print(next(friend))      #b  
#print(next(friend))   #3 

for w in friend:
    print(w,end="  ") #print single line

