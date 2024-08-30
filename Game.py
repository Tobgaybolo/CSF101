# Encapsulation: Character class that encapsulates attributes and behaviors common to all characters in the game.
class Character :
    def __init__(self, name):
        # Encapsulation: Attributes specific to each character are defined here.       
        self.name = name # The name of the character 
        self.health = 100 # Dafault health count
        self.inventory = [] # Empty list to hold items the character collects

    def describe(self):
        print(f"Charater name: {self.name}") # Prints the character's name
        print(f"Health: {self.health}") # Prints the character's health
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}") # Prints the character's inventory status
    
    def take_damage(self, amount):
        self.health -= amount # Decreases the health by e damage amount
        if self.health < 0:
            self.health = 0 # This ensures that the health doesn't drop below 0
        # Prints out the damage taken by the character and updated health status
        print(f"{self.name} has taken {amount}% of damage. Health is now {self.health}%")


    def pick_item(self, item):
        self.inventory.append(item) # Adds item to the inventory list
        # Prints out that the item was picked
        print(f"{self.name} has picked up {item}")

# Composition: as there is "Character" objects and a dictionary of Scenes.
# Adventure class that encapsulates the game world, including characters and scenes.  
class Adventure:
    def __init__(self):
        self.characters = [] # List to store the characters in the play
        self.scenes = {} # Dictionary to store the scenes and their descriptions
    
    def add_character(self, character):
        self.characters.append(character) # Adds a character to the list
        # Prints that the cahracter has joined the adventure
        print(f"Character {character.name} has joined the adventure.")


    def add_scene(self, name, description):
        self.scenes[name] = description # Store the scene's description using the scene's name as the key
        
    def play_scene(self, name):
        if name in self.scenes:
            # If the scene exists, print out it's name and description
            print(f"Scene: {name}")
            print(self.scenes[name])
        else:
            # If the scene doesn't exists, print out an error message
            print(f"The scene {name} does not exist.")

# Inheritance: Hero class that inherits from the Character class.
class Hero(Character):
    # Inheritance: Hero inherits all attributes and methods from Character, but can have additional methods or override existing ones.
    def heal(self, amount):
        self.health += amount # Increaces the health by specific amount

# Polymorphism: because it is a different class with  methods with the same name but different implementations.
# Inheritance: Villain class that also inherits from the Character class.
class Villain(Character):
    # Villain class that also inherits from the Character class.
    def describe(self):
         # Prints a villain-specific description including health and inventory.
        print(f"{self.name} is a fearsome villain with {self.health} health and the following items: {', '.join(self.inventory) if self.inventory else 'Empty'}.") 

# Creating instances of Hero and Villain 
archer = Hero("Archer") # Creating a Hero object named Archer
goblin = Villain("Goblin") # Creating a Villain object named Goblin

# Creating an instance of the Adventure class
adventure = Adventure()

# Adding scenes to the adventure
adventure.add_scene("Forest","You are in a dark forest. There's a shiny object on the ground.")
adventure.add_scene("Cave", "The cave is dark and you can hear growling.")

# Adding characters to the adventure
adventure.add_character(archer)
adventure.add_character(goblin)

# Playing the "Forest scene"
adventure.play_scene("Forest")

# Hero picks up an item
archer.pick_item("Shiny Sword")
archer.describe() # Describe the Hero's current state

# Playing the adventure scene
adventure.play_scene("Cave")

# Hero takes damage
archer.take_damage(20)

# Describe the Hero's current state after taking the damage.
archer.describe()



