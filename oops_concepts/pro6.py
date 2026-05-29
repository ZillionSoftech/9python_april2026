def employee(**kwargs):
    for data in kwargs.items():
        print(data)

employee(id=101, salary=567890,desig="dev",name="user")