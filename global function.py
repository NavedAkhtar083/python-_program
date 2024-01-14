a=10
def showfun():
    a=20
    print("local variable",a)
    x=globals()['a']
    print("x;",x)
showfun()
print("global variable",a)