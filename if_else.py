def fun():
    xx=300
    if xx!=0:
        print("xx is not zero")
    elif xx>0:
        print("xx is positive number")
        if xx%2==0:
                print("xx is even number")
                xx+=1
                for i in range(0,xx):
                    print(i)
    else:
        print("xx is negative number")
fun()
