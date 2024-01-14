#passing array to  function 
from array import*
def show(a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
a=('i',[101,102,103,104])
show(a)