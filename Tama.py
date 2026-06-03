from random import randint

class Tamagochi: 
    def __init__(self, happiness = 30, hunger = 50, mess = 0, age = 1, alive = True):
        self.name = input("Vad ska dit djur heta?: ")
        self.happiness = happiness
        self.hunger = hunger
        self.mess = mess
        self.age = age
        self.alive = alive
        
    
    def action(self):
        while self.alive == True:

            print(f"Namn: {self.name}, Ålder: {self.age}, Glädje: {self.happiness}, Hunger: {self.hunger}, Smutsighet: {self.mess}")
        
            choice = input("Vad vill du göra? Skriv nummer för att välja, enter för att ignorera. 1:Leka 2:Städa 3:Mata - ")
            if choice == "1":
                self.happiness += 20
                print(f"{self.name} blev glad av att leka!")

            elif choice == "2":
                self.mess -= 2
                print(f"{self.name} blev renare!")

            elif choice == "3":
                self.hunger += 40
                print(f"{self.name} blev mättare!")

            else:
                print(f"Du ignorerar {self.name}")

            self.age += 1
            self.hunger -= 10
            self.happiness -= 10
            self.mess += 1

            if randint(1,50) == 1:
                self.alive = False
                print(f"{self.name} Hade en olycka och dog")
            if self.hunger == 0:
                self.alive = False
                print(f"{self.name} svalt till döds")
            if self.happiness == 0:
                self.alive = False
                print(f"{self.name} blev deppad och dog")
            if self.mess == 10:
                self.alive = False
                print(f"{self.name} blev sjuk och dog")


while True:
    pet = Tamagochi()
    Tamagochi.action(pet)