a=5
for i in range(a):
    num=1
    print(num,end=" ")
    for j in range(1,i+1):
        num=num* (i-1+j)//j
        print(num, end=" ")
        
        print()