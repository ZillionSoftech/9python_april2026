num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
result = num1 + num2
print(result)
file=open("abc.txt","w")
file.write(str(result))
file.close()