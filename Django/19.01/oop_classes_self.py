class Person:
    age = 44
    name = "Barry"

    def test(self):
        print("test")

    def get_details(self):
        print("name", self.name, "age", self.age)

    def set_details(self, name, age=10):
        self.name = name
        self.age = age


person1 = Person()

# çalışması için class içindeki def'lerin ilk inputu self olmak zorunda.

# person1.test()
# Person.test(person1)

# çalışması için class içindeki def'lerin attiribute'lerinin önüne self gelmeli

# person1.get_details()
# Person.get_details(person1)

person1.set_details("Aaron", 35)
person1.get_details()
