#This program is made by Bryan Liem. This part of the program allows the creation of a new class called ChangePurse
#That can be applied to variables and provides special instructions when used with operators.
#This is called operator overloading.

#Creates a new class called ChangePurse that holds amount details.
class ChangePurse:

#Declares an instance variable. If no number is declared when a variable is set with the class, sets the amount to 0.
    def __init__(self, amount=0):
        self.amount=amount

#Declares special instructions on what to print out if the class variable is printed.
#In this case, it is the amount in U.S. currency form with always a leading two decimal places.
    def __str__(self):
        return (f'${self.amount:.2f}')

#Defines a new function when called, adds a specific amount into the instance variable.
#Also adds nothing when no number is called.
    def addChange(self, amount=0):
        self.amount += amount

#Defines a new function when called, removes a specific amount into the instance variable.
#Also subtracts nothing when no number is called.
    def removeChange(self, amount=0):
        self.amount -= amount

#Declares special instructions that allows two variables of the same class to be compared.
#This special function returns true if the current amount of the variable is less than the amount of the other variable.
    def __lt__(self, purse):
        if (self.amount < purse.amount):
            return True
        else:
            return False

#This special function returns true if the current amount of the variable is more than the amount of the other variable.
    def __gt__(self, purse):
        if (self.amount > purse.amount):
            return True
        else:
            return False

#This special function returns true if the current amount of the variable is equal to the amount of the other variable.
    def __eq__(self, purse):
        if (self.amount == purse.amount):
            return True
        else:
            return False