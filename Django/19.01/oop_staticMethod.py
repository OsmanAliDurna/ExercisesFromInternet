class Person:
    name = "Barry"
    age = 44

    def set_details(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_details(self):
        print("name -> ", self.name, "age -> ",
              self.age, "location -> ", self.location)

    @staticmethod
    def salute():
        print("Hi there!")


person1 = Person()
person1.salute()
