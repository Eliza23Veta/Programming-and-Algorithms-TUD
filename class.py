class IceCream:
    def __init__(self, name, number_of_balls, taste, colour):
        self.name = name
        self.number_of_balls = number_of_balls
        self.taste = taste
        self.colour = colour

    def __str__(self): 
        return f"{self.name} icecream has {self.number_of_balls} balls, {self.taste} taste and {self.colour} colour."

    def IsYummy (self):
        return f"{self.name} is yummy!"

chocoland = IceCream("ChocoLand", 3, "chocolate", "brown")

berry = IceCream("Berry", 5, "blueberry", "blue")

print(chocoland)
print(chocoland.IsYummy())
print(berry)
print(berry.IsYummy())

dir(IceCream) 

