#check the given element is exist or not
#using loop
list_name=[10,3,8,2,6,9]
for i in list_name:
    if(i==8):
        print("element exist in list")
    else:
        print("element not exist in list")
#using in
if(7 in list_name):
    print("element exist")
else:
    print("element not exist")
