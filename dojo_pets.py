



class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        print (f"{self.name}'s energy increased by 25!")
        print(f"{self.name} energy is {self.energy}")
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print (f"{self.name}'s energy increased by 5 and health increased by 10!")
        print(f"{self.name} energy is {self.energy} and health is {self.health}")

    def play(self):
        self.health += 5
        print (f"{self.name}'s health increased by 5!")
        print(f"{self.name} health is {self.health}")

    def noise(self):
        print(f"{self.name} lets outs a noise!")



class Dog(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

