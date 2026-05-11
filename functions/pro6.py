numbers = [10,20,40,30,80,50,80]

new_list = []

for i in numbers:
    new_num = lambda x:x*x
    new_list.append(new_num(i))

print(new_list)