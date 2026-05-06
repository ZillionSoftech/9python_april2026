# simple if 
# if else
# nested if else
# if elif else

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

optr = input("Enter operator symbol : ")

if optr=="+":
    result = num1 + num2
    print(f"Additon of two number : {result}")

elif optr=="-":
    result = num1 - num2
    print(f"Subtraction of two numbers : {result}")

elif optr=="*":
    result = num1 * num2
    print(f"Multiplication of two numbers : {result}")

elif optr=="/":
    result = num1 / num2
    print(f"Division of two numbers : {result}")

else:
    print("You entered wrong symbol")

