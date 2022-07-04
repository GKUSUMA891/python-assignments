for p in range(0,20):
    print(p,end=" ")'''
man=36
def sum():
    global man   #by using global keyword change the value of global
    man=80
    print(man)
    return man*2
print(man)
var=sum()
print(man,var)
