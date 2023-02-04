from random import randint

class Die():
    """This class is to represent a die"""
    
    def __init__(self, sides = 6) -> None:
        """Create a die and its sides"""
        self.sides = sides

    def roll(self) -> int:
        """Represent a row of the dice and return its value"""
        return randint(1,self.sides)