class Employee:
    def __init__(self,id, name, desig, salary):
        self.id = id
        self.name = name
        self.desig = desig
        self.salary = salary
        self.__data=100

    def __str__(self):
        return f"Id : {self.id} | Name : {self.name} | Desig : {self.desig} | Salary : {self.salary}"


emp = Employee(101,"user1","developer",567568)
print(emp)

emp1 = Employee(102,"user2","designer",45679)
print(emp1)

# print(emp1.desig)
# print(emp1.__data)

# base 4
# positional
# keyword
# variable length positional argument
# variable length keyword argument
# lambda function
