# creating a class with construction
class employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def employee_details(self):
        print("name of employee is",self.name)
        print("age of employee is", self.age)
        print("salary of employee is", self.salary)
        print("gender of employee is", self.gender)
pi = employee("yogee",29,100000,"male")
pi.employee_details()
