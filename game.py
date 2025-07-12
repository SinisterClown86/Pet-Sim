import time
import random
import os

# ========== UTILS ==========
def slow_print(text, delay=0.02):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ========== CLASSES ==========
class Pet:
    def _init_(self, name, species):
        self.name = name
        self.species = species
        self.level = 1
        self.exp = 0
        self.health = 100
        self.max_health = 100
        self.hunger = 0
        self.happiness = 100
        self.energy = 100
        self.strength = 5
        self.agility = 5
        self.intelligence = 5
        self.alive = True

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Level: {self.level} | EXP: {self.exp}/100")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Stats -> STR: {self.strength} | AGI: {self.agility} | INT: {self.intelligence}")

    def feed(self):
        if self.hunger <= 0:
            print(f"{self.name} is not hungry.")
        else:
            self.hunger = max(0, self.hunger - 20)
            self.happiness += 5
            print(f"You fed {self.name}. Hunger decreased!")

    def train(self):
        if self.energy < 20:
            print(f"{self.name} is too tired to train.")
            return
        stat = random.choice(['strength', 'agility', 'intelligence'])
        setattr(self, stat, getattr(self, stat) + 1)
        self.energy -= 20
        self.hunger += 10
        self.happiness -= 5
        print(f"{self.name} trained and increased their {stat}!")

    def sleep(self):
        if self.energy >= 100:
            print(f"{self.name} is already full of energy.")
        else:
            self.energy = 100
            self.happiness += 10
            print(f"{self.name} took a nap and feels refreshed!")

    def play(self):
        if self.energy < 10:
            print(f"{self.name} is too tired to play.")
            return
        self.happiness += 10
        self.energy -= 10
        self.hunger += 5
        print(f"You played with {self.name}. They're happier!")

    def adventure(self):
        if self.energy < 30 or self.health < 30:
            print(f"{self.name} isn't in good shape for an adventure.")
            return

        self.energy -= 30
        self.hunger += 15
        encounter = random.choice(['enemy', 'treasure', 'nothing'])

        if encounter == 'enemy':
            result = self.battle()
            if result:
                self.gain_exp(30)
        elif encounter == 'treasure':
            reward = random.choice(['strength', 'agility', 'intelligence'])
            setattr(self, reward, getattr(self, reward) + 2)
            print(f"{self.name} found a magical artifact! {reward} increased!")
        else:
            print(f"{self.name} wandered around but found nothing.")

    def battle(self):
        enemy_level = random.randint(self.level, self.level + 2)
        enemy_health = 50 + enemy_level * 10
        print(f"A wild enemy appears! Level {enemy_level} beast!")

        while self.health > 0 and enemy_health > 0:
            damage = self.strength + random.randint(0, 5)
            enemy_damage = enemy_level * 5 + random.randint(0, 5)
            print(f"{self.name} attacks for {damage} damage!")
            enemy_health -= damage
            if enemy_health <= 0:
                print("Enemy defeated!")
                return True
            print(f"Enemy attacks for {enemy_damage} damage!")
            self.health -= enemy_damage
            if self.health <= 0:
                print(f"{self.name} fainted!")
                self.alive = False
                return False
        return False

    def gain_exp(self, amount):
        self.exp += amount
        if self.exp >= 100:
            self.exp -= 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.strength += 2
        self.agility += 2
        self.intelligence += 2
        print(f"{self.name} leveled up to {self.level}!")

    def tick(self):
        if self.hunger >= 100:
            self.health -= 5
            print(f"{self.name} is starving! Health is decreasing!")
        if self.happiness <= 0:
            self.health -= 2
            print(f"{self.name} is very unhappy! Health is decreasing!")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has passed away...")

# ========== MAIN GAME ==========
def choose_pet():
    name = input("Name your pet: ")
    species = input("What species is your pet (dragon, cat, dog, alien)? ")
    return Pet(name, species)

def main_menu(pet):
    while pet.alive:
        clear()
        print(f"🐾 {pet.name}'s Adventure 🐾")
        pet.display_stats()
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Train")
        print("3. Sleep")
        print("4. Play")
        print("5. Go on Adventure")
        print("6. Exit Game")

        choice = input(">> ")
        clear()

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.train()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.play()
        elif choice == '5':
            pet.adventure()
        elif choice == '6':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

        pet.tick()
        input("\nPress Enter to continue...")

# ========== START GAME ==========
def intro():
    clear()
    slow_print("Welcome to Terminal Pet Adventure!")
    time.sleep(1)
    slow_print("Adopt your pet, care for it, and explore the world.")
    time.sleep(1)
    input("\nPress Enter to begin your journey...")

def run_game():
    intro()
    pet = choose_pet()
    main_menu(pet)

run_game()
