num1 = int(input("Enter frist number : "))
num2 = int(input("Enter second number : "))
result = num1 + num2
print(result)

file=open("bill.txt","w")
file.write(str(result))
file.close()


# w=> write
# r => read data
# a => append


with open("bill.txt","w") as f:
    f.write("Working fine")