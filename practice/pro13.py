class A:
    def __init__(self):
        print("A")

    def disp(self):
        print("Disp function")

class B(A):
    def __init__(self):
        print("B")

    def disp(self):
        super().disp()
        print("inside b class disp method")

obj = B()
obj.disp()