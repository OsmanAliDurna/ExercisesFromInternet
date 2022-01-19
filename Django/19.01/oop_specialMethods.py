class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name}      Age : {self.age}"

    def get_details(self):
        print("name -> ", self.name, "age -> ",  self.age)


person1 = Person("Barry", 44)
person1.get_details()

lst = [1, 2, 3]
print(lst)

print(person1)
