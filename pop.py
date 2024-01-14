import array
mystring=array.array('i',[101,102,103,104,105])
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1
print("after the pop method ")
mystring.pop(2)
mystring.pop(3)
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1