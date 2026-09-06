class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + " makes a sound.")

class dog(animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(self.name + " the " + self.breed + " barks.")


dog1 = dog("Buddy", "Golden Retriever")
dog1.speak()
dog1.bark()