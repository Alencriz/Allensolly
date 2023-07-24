num=int(input("enter 3 number:"))
sum=0
for digit_str in num:
    a=int(digit_str)
    sum+=a**2
print(sum)    