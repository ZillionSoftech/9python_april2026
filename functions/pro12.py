# map(task,data)
# list=[10,20,30,40,60]

list_data = [1,2,3,4,5]
data=map(lambda num:num*num, list_data)

print(type(data))
for item in data:
    print(item)