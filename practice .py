def func(a,b):
    if a==0:
        return b
    else:
        return func(a-1,a+b)

print(func(5,5))