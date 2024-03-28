lower=2
upper=5

for num in range(lower,upper+1):
    flag=1
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                flag=0
                break
        if flag==1:
            print(num)
