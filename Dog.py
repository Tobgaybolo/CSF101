class Dog:
    def __init__(self, name, color, Age):
        self.name = name
        self.color = color
        self.Age = Age

    def bark(self):
        return f" {self.name} {self.color} {self.Age} bark"
    
Nima = Dog("Nima", "yellow", "5")
Dawa = Dog("Dawa", "brown", "7")
Bruno = Dog("Bruno", "black", "4")

print(Bruno.bark())
        