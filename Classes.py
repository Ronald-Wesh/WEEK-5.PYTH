class SuperHero:
    def __init__(self,name,age,superpower):
        self.name=name
        self.age=age
        self.superpower=superpower

    def save_the_world(self):
        print(f"{self.name} saves the World")
    def fly(self):
        print(f"{self.fly} is one of his abilities")
    def show_superpower(self):
        print(f"{self.superpower} is one of his superpowers")
#Inheritance
class Superman(SuperHero):
    def __init__(self,name,age,agility,city):
        super().__init__(name,age,superpower="Super Strength")
        self.agility=agility
        self.city=city
    #Polymorphism
    def save_the_world(self):
        print(f"{self.name} saves the {self.city} from the bad guys")
    def fly(self):
        print(f"{self.name} flies over the {self.city}")
        
#Example usage
Hero=SuperHero("Flash",30,"Super Speed")
Hero2=Superman("Clark","27","Agility","Nairobi")
Hero.fly()
Hero2.fly()
Hero.save_the_world()
Hero2.save_the_world()

        




