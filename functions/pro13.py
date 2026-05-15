# map(task,data)
# list=[10,20,30,40,60]

list_data1 = [1,2,3,4,5]
list_data2 = [1,2,3,4,5]
data=map(lambda num1,num2:num1+num2, list_data1,list_data2)

print(type(data))
for item in data:
    print(item)