from functools import reduce


# data=reduce(lambda x,sum:sum+x,[1,2,3,4,5,6],0)
# print(data)

list_data = [1,2,3,4,5,6,7,8,9,10]
result=reduce(lambda sum,x:sum+x,list_data,0)
print(result)