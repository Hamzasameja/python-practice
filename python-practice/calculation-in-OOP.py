class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

    def can_vote(self):
        if self.age >= 18:
            return True
        else:
            return False

person1 = person("Hamza", 30)
person2 = person("Ali", 15)

print(person1.name + " can vote: " + str(person1.can_vote()))
print(person2.name + " can vote: " + str(person2.can_vote()))

person1.greet()
person2.greet()