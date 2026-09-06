class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")

class Dog(Animal):
    def speak(self):
        print(self.name + " barks.")

class Cat(Animal):
    def speak(self):
        print(self.name + " meows.")

class cow(Animal):
    def speak(self):
        print(self.name + " moos.")

animals = [Dog("Buddy"), Cat("Whiskers"), cow("Bessie")]
for animal in animals:
    animal.speak()