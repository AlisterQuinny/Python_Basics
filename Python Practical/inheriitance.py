print("37 Alister Quinny")
class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def bark(self):
        return"{self.name} says woof!"
Dog1 = Dog("Buddy")
print(Dog1.bark())
