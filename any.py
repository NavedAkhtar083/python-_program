from numpy import*
a=array([100,102,103,104,107,105])
b=array([100,108,109,104,109,110])
c=where(a<b,a,b)
print(c)