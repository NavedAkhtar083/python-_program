from  numpy import*
a=array([100,0,104,105,0,106])
b=copy(a)
a[2]=108
b[1]=104
print(a)
print(b)
print("a",id(a))
print("b",id(b))