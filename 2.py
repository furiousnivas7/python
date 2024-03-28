num=int(input("enter the num:" ))
factorial=1
if (num<0):
    print(negative)
elif(num==0):
    print("the factoral is 1")
else:
    i=1
    while (i<=num):
        factorial=factorial*i
        i=i+1
    print("the factorial is", factorial)
        
    
