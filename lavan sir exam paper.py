num=int(input("enter the number:" ))
x=0
y=1
while(num>=x):
    print(x)
    z=x+y
    x=y
    y=z

n=5
i=1;j=0
while(i<=n):
    while(j<=i-1):
        print("*",end=" ")
        j+=1
    print("\r")
    j=0;i+=1
