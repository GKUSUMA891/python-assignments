'''list=[10,23,4,6,7]
item=mul(list)
print(item)'''

def mul_list(items):
    mul=1
    for i in items:
        mul=mul*i
    return mul
items=[10,20,33,5]
print(mul_list(items))
