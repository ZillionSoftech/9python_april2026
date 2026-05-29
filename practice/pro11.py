def operation(a):
    def inner(b):
        return a + b

    return inner

x = operation(10)

print(x(5))