"""
This is the main Inventory

Choose food, add/remove, quantity (to be moved @laterdate)
"""

#from __future__ import barry_as_FLUFL

__Inventory__ = {'tomatoes' : 5}
__version__ = '0.1'
__author__ = 'Spencer Norwick'

#import os
#import sys
 
print(Inventory)					 

#First user input. Sets user_food variable = string which user types in
user_food = input("What food do you want to update?")

#check to see if user input string is a key in Inventory dictionary
if user_food in Inventory :	
	#Second user input
	user_action= input("Do you want to 'add' or 'remove' %s from Inventory?" % user_food)
	if user_action== "add":
		#Third user input
		user_quantity = input("How many do you want to %s?" % user_action)
		#add integer of user input to item quantity
		Inventory[user_food] += int(user_quantity)
	elif user_action== "remove" :		
		#Third user input (alternate)
		user_quantity = input("How many do you want to %s?" % user_action)
		#remove integer of user input from item quantity
		Inventory[user_food] -= int(user_quantity)
	else:
		#message to user if they don't type 'add' or 'remove'
		print("Please type 'add' or 'remove' to update the quantity of %s in Inventory" % user_food)
else :
	#message to user if user_food is not a key in Inventory dict
	print("Sorry, there are no %s in Inventory" % user_food)

print(Inventory)

#next, I'll give the option to add a new item to inventory. Either at beginning as alternative option to "what food do you want to update" or after the user tries to update something and gets the error message above. 
