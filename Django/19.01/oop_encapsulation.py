class Person:
    company = "Clarusway"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._id = 5000
        self.__id2 = 4000

    def __str__(self):
        return f"Name : {self.name}      Age : {self.age}"

    def get_details(self):
        print("name -> ", self.name, "age -> ",  self.age)


person1 = Person("Barry", 44)
print(person1._id)

person1._id = 6000
print(person1._id)

# print(person1.__id2)          Hata verir.
# print(person1._Person__id2)   ille de ulaşılmak istenirse yapılabilinen yol budur.
