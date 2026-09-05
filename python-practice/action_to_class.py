class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

    def birthday(self):
        self.age += 1
        print("Happy Birthday! You are now " + str(self.age) + " years old.")

person1 = person("Hamza", 30)
person1.greet()
person1.birthday()
person1.greet()