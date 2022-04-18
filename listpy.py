def swapplist(onelist):
    onelist[0],onelist[-1]=onelist[-1],onelist[0]
    return onelist
onelist=[10,20,30,45,67,89]
print(swapplist(onelist))
print(onelist[0])
print(onelist[-1])
print(onelist[4])
