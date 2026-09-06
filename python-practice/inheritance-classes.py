class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")

class dog(animal):
    def bark(self):
        print(self.name + " says Woof!")

dog1 = dog("Buddy")
dog1.speak()
dog1.bark()