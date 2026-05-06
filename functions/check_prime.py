# 7

# 7
# 1,7
# 2,3,4,5,6

# 7/2 !=0 it may prime
# 7/3 !=0 it may prime
# 7/4 !=0 it may prime
# 7/5 !=0 it may prime
# 7/6 !=0 it is prime


num = int(input("Enter a number to check prime or not : "))
status = True

for i in range(2,num):
    if num%i==0:
        status=False

if status==True:
    print(f"Number is prime number : {num}")
else:
    print(f"Number is not prime number : {num}")
        
