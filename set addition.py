txt=input("enter:" )
i=0
x=len(txt)-1
for a in range (x, 0,-1):
    if(txt[i]==txt[a]):
        if(i>a):
            print("i")
            
        else:
             i+=1
             continue
        i=i+1
    else:
        print("not")

