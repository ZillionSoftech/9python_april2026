num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter fourth number : "))

if num1>num2:
    if num1>num3:
        if num1>num4:
            print(f"First number is greater : {num1}")
        else:
            print(f"Fourth number is greater : {num4}")
    else:
        if num3>num4:
            print(f"Third number is greater : {num3}")
        else:
            print(f"Fourth number is greater : {num4}")
else:
    if num2>num3:
        if num2>num4:
            print(f"Second number is greater : {num2}")
        else:
            print(f"Fourth number is greater : {num4}")
    else:
        if num3>num4:
            print(f"Third number is greater : {num3}")
        else:
            print(f"Fourth number is greater : {num4}")