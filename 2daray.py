from numpy import*
n=int(input("enter the number of element rows :"))
m=int(input("enter the number of element of column:"))
a=zeros((n,m),dtype=int)
u=len(a)
print(a)
for i in range(u):
    for j in range(len(a)):
        x=int(input("enter the element:"))
        a[i][j]=x
        
for r in a:
    for c in r:
        print(c)
print(a)