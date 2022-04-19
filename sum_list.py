'''def sum_list(items):
    sum_list1=[10,20,35,60]
    sum_list1=0
    for i in items:
       sum_list1=sum_list1+i
    return sum_list1
print(sum_list1())'''

list=[10,20,35]
s=sum(list)
print(s)

def sum_list(items):
    sum_numbers = 0
    for i in items:
        sum_numbers=sum_numbers+i
    return sum_numbers
items=[1,2,8]
print(sum_list(items))
