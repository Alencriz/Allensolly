a=0
num=int(input("enter a number: "))
for i in range (1,num+1):
    for j in range(1,i+1):
        if j==1 or j==i:
            print(1,end=" ")
        else:
            print(a+i-1,end=" ")    
    print()        