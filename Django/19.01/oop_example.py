class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.movements = []

    def add_movement(self, number, date, explain):
        self.movements.append(
            {"amount": number, "date": date, "explain": explain})

    def all_movements(self):
        return [print(i["date"], i["amount"], i["explain"]) for i in self.movements]

    def balance(self):
        balance = 0
        for i in self.movements:
            balance += i["amount"]
        print(balance)
        # print(sum(i["amount"] for i in self.movements))


person1 = Person("Barry", 44)

person1.add_movement(-50, "19.01.2022", "buy gasoline")
person1.add_movement(1000, "15.01.2022", "salary")
person1.add_movement(-500, "16.01.2022", "rent")
person1.add_movement(-100, "17.01.2022", "electric bill")
person1.add_movement(-200, "18.01.2022", "gas bill")

person1.all_movements()
person1.balance()
