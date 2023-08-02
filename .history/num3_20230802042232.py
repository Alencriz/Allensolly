a=int(input("Enter the row size:"))
for i in range(1,a+1):
    for i in range(a+1,i,-1):
        print(i,end="")
    print(" ")
