i=2
def myfun():
 global i
 while i<6:
   i+=1
   print("my function",i)
myfun()
print(i)
  