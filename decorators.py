def decorator(func):
   def inner_decorator(x,y):
       if x<30:
           x = 0
       if y<30:
           y = 0
       return func(x,y)
   return inner_decorator 

def add(a,b):
   res = a + b
   return res

add = decorator(add)
print(add(20,30))
print(add(-10,5))
