class my_friend:
    def __iter__(arg):
        arg.a=1
        return arg
    def __next__(arg):
        if arg.a<=20:
            x=arg.a
            arg.a+=1
            return x
        else:
             raise stopiteration
self=my_friend()
selfy=iter(self)
for i in selfy:
    print(i)
#print(next(selfy))   
#print(next(selfy))
#print(next(selfy))'''
