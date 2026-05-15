from functools import reduce


# data=reduce(lambda x,sum:sum+x,[1,2,3,4,5,6],0)
# print(data)

def sum(sum, num):
    print(f"num : {num} and sum : {sum}")
    return sum+num

list_data = [1,2,3,4,5,6,7,8,9,10]
result=reduce(sum,list_data,0)
print(result)