def show(a,b):
    yield a
    yield b
result=show(5,8)
print(result)
print(result(type))
print(next(result))
print(next(result))