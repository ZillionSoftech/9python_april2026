# simple if
# if else
# nested if else
# if elif else




# nested if else
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))
if num1>num2:
    if num1>num3:
        print(f"First number is greater : {num1}")
    else:
        print(f"Third number is greater : {num3}")
else:
    if num2>num3:
        print(f"Second number is greater : {num2}")
    else:
        print(f"Third number is greater : {num3}")

