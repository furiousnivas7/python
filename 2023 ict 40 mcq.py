def func1(a,b):
    return a+b
def func2(a,b):
    return a*b
result=func1(3,func2(2,4))
print(result)


a=10
b=4
c=7
ans=a%b+c//(a-b)
print(ans)


def modifi_string(input_string):
    input_string+=" world"
    return input_string
text="hello"
print(modifi_string(text))
print(text)


original_list= [1, 2, 3, 4, 5]
new_list=original_list.copy()
new_list.clear()
original_list.append(6)
print(original_list)
print(new_list)


i = 7
while i > 0:
    i -=3
    print ("*")
    if i<=2:
        break
    else:
        print('*')
        
for i in range (1, 4):
    for j in range (1, 1+ 1):
        print (j*i, end=' ') 
    print ()
