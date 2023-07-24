ip1=input("enter nums:")
for num in ip1.split():
    list1=int(num)

ip2=input("enter nums:")
for num in ip2.split():
    list2=int(num)

a=list(set(ip1) & set(ip2))
print(a)