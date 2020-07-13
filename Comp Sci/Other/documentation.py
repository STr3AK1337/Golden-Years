#-----------------------------------------------------------------------------
# Name:        Documentation and basic knowledge (documentation.py)
# Purpose:     Shows understanding of documentation and python
#
# Author:      Abtin Tabrizi
# Created:     12-Sept-2019
# Updated:     19-Sept-2019
#-----------------------------------------------------------------------------
import random


class Cat:
    """
	A class for cat objects

    Creates cats that hold values for name, colour and breed
	
	Attributes
	----------
	name : str
		The name of the cat
	colour : str
		The colour of the cat
	breed : str
		The breed of the cat
		
	Methods
	-------
	none
	"""

    def __init__(self, name, colour, breed):
        """
        A constructor to build the cat object

        Creates a cat object with name, colour and breed attributes

        Parameters
        ----------
        name : str
            The name of the cat
        colour: str
            The colour of the cat
        breed: str
            The breed of the cat
        """

        self.name = name
        self.colour = colour
        self.breed = breed


def menu():
    """
    Prints the program's main menu

    Parameters
    ----------
    none

    Returns
    -------
    none
    """

    print("\n1. Flip a coin\n2. Adopt a cat\n3. Create or add to a grocery list\n4. Exit")
    return

def coinFlip(amount):
    """
    Flips coins and says what it lands on

    Flips a coin by randomly picking a side for as many times (up to 100) that the user wants  

    Parameters
    ----------
    amount : int
        The amount of coins to be flipped

    Returns
    -------
    list
        Returns a list with all the results of which side each coin landed on
    """
    
    sides = []
    for x in range(0, amount):
        side = random.randint(1, 2)
        if side == 1:
            sides.append("Heads")
        elif side == 2:
            sides.append("Tails")
    return sides

catDict = {}
userOption = 0
cNumber = 0
itemList = []
amountList = []
while True:
    menu()
    while userOption < 1 or userOption > 4:
        userOption = int(input("\nSelect an option: "))

    if userOption == 1:
        amount = 0
        while amount < 1 or amount > 100:
            amount = int(input("\nEnter the number of coins you want to flip (100 max): "))
        sides = coinFlip(amount)
        print(sides)
        userOption = 0

    elif userOption == 2:
        n = -1
        while n < 0 or n > 5:
            n = int(input("\nEnter the number of cats you want to adopt (5 max, 0 to cancel): "))
            if n == 0:
                break
        for catNumber in range(0, n):
            name = str(input("\nName your cat: "))
            breed = str(input("Enter the breed of your cat: "))
            colour = str(input("Enter the colour of your cat: "))
            globals()["cat%s" % cNumber] = Cat(name, colour, breed)
            catDict["cat%s" % str(cNumber+1)] = [name, colour, breed]
            print("\nCongratulations you've adopted a " + colour + " " + breed + " named " + name)
            cNumber = cNumber + 1
        print(catDict)
        userOption = 0
            
    elif userOption == 3:
        item = input("\nWhat item would you like to add to your grocery list? ")
        iAmount = input("How many would you like to buy? ")
        itemList.append(item)
        amountList.append(iAmount)
        print("\nYour current grocery list is:")
        for i in range(0, len(itemList), 1):
            print(itemList[i] + ": " + amountList[i])
        userOption = 0

    elif userOption == 4:
        print("\nExiting...")
        break