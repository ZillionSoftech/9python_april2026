# function with no argument and no return value

# function with no argument and return value
# def visit_mamas_house():
#     mama = 500
#     nani = 1000
#     mami = 150
#     amount = mama + nani + mami
#     return amount


# money=visit_mamas_house()
# print(f"Total money got : {money}")

# function with argument and no return value

# def visit_sisters_house(amount):
#     print(f"Money and Gifts Taken by sister : {amount}")


# money=1500
# visit_sisters_house(money)


# function with argument and return value
def visit_in_laws_family(money):
    print(f"Gifts taken by in-laws family : {money}")
    amount = money + 1000
    return amount


amount=visit_in_laws_family(100)
print(amount)