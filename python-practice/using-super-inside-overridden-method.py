class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak()  # Call the parent class's speak method
        print(self.name + " also barks loudly!")

dog1 = Dog("Buddy")
dog1.speak()  # Output: Buddy makes a sound. Buddy also barks loudly!