from array import*
mystring=array('i',[101,102,103,104,105])
array=array('i',[106,108,109])
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1
print("after the extend method")
mystring.extend(array)
n=len(mystring)
i=0
while(i<n):
    print(mystring[i])
    i+=1

