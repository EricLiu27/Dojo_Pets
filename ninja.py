from Dojo_Pets.ninja import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(pet, type, tricks= "roll over", health = 100, energy= 100)
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"You go for a walk and play with {self.pet.name}")
        self.pet.play()

    def feed(self):
        print(f"You feed {self.pet.name} the {self.pet_food}!")
        self.pet.eat()
    
    def bathe(self):
        print(f"You bathe {self.pet.name}!")
        self.pet.noise()


dog_1 = Pet("Pico", "golden retriever", "roll over", 100, 100)

ninja_1 = Ninja("Eric", "Liu", "Pico", "puppy chow", "best brand")

ninja_1.feed()
ninja_1.walk()
ninja_1.bathe()