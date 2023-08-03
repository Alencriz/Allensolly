a=5
for i in range(a):
    #num=1
    for j in range(1,i+2):
        print(num, end=" ")
        num=num*(i+1-j)
        print()