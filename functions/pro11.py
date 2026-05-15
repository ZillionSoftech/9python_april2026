# map(task,data)
# list=[10,20,30,40,60]
def square(num):
    return num*num

list_data = [1,2,3,4,5]
data=map(square, list_data)


for item in data:
    print(item)