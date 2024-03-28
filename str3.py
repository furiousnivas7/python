f1=open("a.txt",'r')
f2=open("b.txt",'w')
for line in f1:
    items=line.strip().split(",")
    tot=int(items[1])+int(items[2])+int(items[3])
    print(items[0],tot,file=f2)
f1.close()
f2.close()
