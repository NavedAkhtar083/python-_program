import array
mystring=array.array('i',[101,102,103,104,105])
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1
print("after the insert method ")
mystring.insert(2,106)
mystring.insert(5,107)
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1