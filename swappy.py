def swapptwo_ele(newlist):
    newlist[0],newlist[-2]=newlist[-2],newlist[0]
    return newlist
newlist=[34,56,778,90,23,56,65]
#print(swapptwo_ele(newlist))
print("before swapping",newlist)
print("after swapping",swapptwo_ele(newlist))
