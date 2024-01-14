st={101:'rahul',102:'raj',103:'shivam'}
print(type(st))
print(st)
print()

i=st.items()
print(i)
print(type(i))
print()

#how to access the dictionary
ist=list(i)
print(ist)
print(type(ist))
print()

print(ist[0])
print(ist[0][0])
for  a in ist :
    for c in  a:
        print(c)