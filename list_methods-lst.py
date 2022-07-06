string="hi friend"
n=string[::-1]
print(n)
a=[10,20,30,40,50,60]
n=len(a)
print("length:",n)
for i in range(n):
    print(i,a[i])'''

#----------------
#copy,append
'''a=[10,20,30,40,50,60,70]
print("a is:",a)
b=a.copy()
print("b is:",b)
b.append(1000)
print(b)'''
#--------------
#for and if
'''num=[10,20,30,40,[12,13,14,15],80]
for i in num:
    if [12,13,14,15] in num:
        print(num)
        if i==num[1]:
            break
print(i)'''
#-----------
#extend,remove,count
'''man=[100,200,300,400,500]
man.extend([300,203,104,105,[1,2,3,4,5],300])
print(man)
man.append(555)
print(man)
man.remove(100)
print(man)
man[2]=180
print(man)
n=man.count(300)
print("count:",n)
