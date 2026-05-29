from multipledispatch import dispatch

@dispatch(int, int)
def disp(num1, num2):
    print(num1, num2)

@dispatch(int, int, int)
def disp(num1, num2, num3):
    print(num1, num2, num3)

disp(10,20)
disp(10,20,30)

def sum(num1, num2):
    print(num1, num2)

def sum(num1, num2, num3):
    print(num1, num2, num3)

sum(10,20,10)

