num=int(input("enter a number: "))
count=True
a=2
while a<=num:
    if num % a==0:
        count=False
    a+=1    
        
            
if count>2:
    print(num,"is not prime")
else:
    print(num,"is a prime")            