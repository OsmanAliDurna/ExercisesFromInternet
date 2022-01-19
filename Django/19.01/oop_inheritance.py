class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}      Age : {self.age}"

    def get_details(self):
        print("name -> ", self.name, "age -> ",  self.age)


class Lang:
    langs = "LANG"

    def __init__(self, langs):
        self.langs = langs

# Bu şekilde başka bir classın özellik ve metotlarını direk alma işlemi kalıtım inheritance oluyor.


class Employee(Person, Lang):

    def __init__(self, name, age, path):
        self.name = name
        self.age = age
        self. path = path


emp1 = Employee("Aaron", 35, "FS")

print(emp1.company)
print(emp1.name)
print(emp1.age)
print(emp1.path)
print(emp1.langs)
