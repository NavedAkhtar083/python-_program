from numpy import*
n=int(input("enter the number of element "))
a=zeros(n,dtype=int)
b=len(a)
for i in range(b):
    x=int(input("enter the element= "))
    a[i] = x
print(a)