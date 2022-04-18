def list_length(newlist):
    listsize=len(newlist)
    return newlist
newlist=[100,23,4,5,6,7,8,9]
#first way
print(len(newlist))
newlist.append(20)
print(len(newlist))
print(list_length(newlist))
#print(listsize)
#second way
c=0
for i in newlist:
    c=c+1
    print("length of" ,i ,"is:",len(newlist))
