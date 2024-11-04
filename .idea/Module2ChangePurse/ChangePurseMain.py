#This program is made by Bryan Liem. This part of the program imports Purse.py for the classes and tests its normal
#and special instructions.
import Purse

#Sets two variables to the ChangePurse class with a specific amount for one of the variables.
#The variables are printed to verify the function works.
purse1 = Purse.ChangePurse()
purse2 = Purse.ChangePurse(7.59)
print(purse1)
print(purse2)

#Adds 5.59 into purse1's amount.
#The variables are printed to verify the function works.
purse1.addChange(5.59)
print(purse1)

#Adds nothing into purse1's amount, then subtracts 1.00 from purse1's amount.
#The variables are printed to verify the function works.
purse1.addChange()
purse1.removeChange(1)
print(purse1)

#Uses three comparison operators
#The variables are printed to verify the function works. Should print in the following order: False, True, False.
print(purse1 == purse2)
print(purse1 < purse2)
print(purse1 > purse2)

#Adds 2.00 into purse1's amount, subtracts 1.00 from purse2's amount, and compares if both amounts are equal, along
#with printing purse2's amount. The variables are printed to verify the function works.
purse1.addChange(2.00)
purse2.removeChange(1)
print(purse1 == purse2)
print(purse2)