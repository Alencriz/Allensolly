a=int(input("Enter the row size:"))
for out in range(1,a+1):
    for i in range(a+1,out,-1):
        print(out,end="")
    print("\r")
