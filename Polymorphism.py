
class Animal:
    def move(self):
        print("The animal is moving")
class Cat(Animal):
    def move(self):
        print("The  Cat is running")
class Dog(Animal):
    print("The dog is barking")
#Example usage
for animal in [Cat(),Dog()]:
    animal.move()

