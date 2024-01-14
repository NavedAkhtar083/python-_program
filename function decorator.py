def myfun():
    def inner():
        print("IF: Before enhancing function ")
        fun()
        print("IF: aAfter enhancing function")
    return inner()
def num():
    print("we will use this function ")
    print("and will enhancing this in decorator ")
result_fun=myfun(num)
result_fun()
