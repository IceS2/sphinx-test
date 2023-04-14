"""
This module only exists to exemplify how to auto document code using Sphinx

"""
import random

def func1(a: int, b: str) -> str:
    if a > 0:
        return b
    else:
        return "a is negative"


class Dice:
    """ This class just defines a Dice with one method: `roll`"""
    def __init__(self, sides: int):
        """Takes as the init parameter the number of sides

        Lorem Ipsum Lorem Ipsum Lorem Ipsum
        Lorem Ipsum

        Parameters
        ----------

        sides: int
            The amount of sides the Dice has. (e.g. `6`)

        Returns
        -------

        Dice
            Object Dice of #sides
        """
        self.sides = sides

    def roll(self) -> int:
        """ Rolls the dice

        It randomly picks a number between 1 and the number of sides of the dice

        Returns
        -------

        int
            Result of the Dice roll
        """
        """ Rolls a dice with n sides"""
        return random.randint(1, self.sides)

