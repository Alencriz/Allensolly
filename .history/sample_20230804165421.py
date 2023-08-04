num = int(input("Enter a number :"))  
f = 0
i = 2
while i <= num / 2:
    if num % i == 0:
        f=1
        break
    i=i+1
    
if f==0:
    print(" is a PRIME number")
else:
    print("not a PRIME number")    