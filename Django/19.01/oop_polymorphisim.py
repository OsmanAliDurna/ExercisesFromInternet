class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}      Age : {self.age}"

    def get_details(self):
        print("name -> ", self.name, "age -> ",  self.age)


class Employee(Person):
    # inheritance ile alınan özelliklerin üzerine yazma işlemi polymorphisim
    def __init__(self, name, age, path):
        super().__init__(name, age)
        self. path = path

    def get_details(self):
        print("name -> ", self.name, "age -> ",
              self.age, "path -> ", self.path)


emp1 = Employee("Aaron", 35, "FS")
emp1.get_details()

