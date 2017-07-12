Inventory = {'tomatoes' : 5}
print(Inventory)

user_food = input("What food do you want to update?")

if user_food in Inventory :
	user_operation = input("Do you want to 'add' or 'remove' %s from Inventory?" % user_food)

	if user_operation == "add":
		user_quantity = input("How many do you want to %s?" % user_operation)
		Inventory[user_food] += int(user_quantity)
	elif user_operation == "remove" :
		user_quantity = input("How many do you want to %s?" % user_operation)
		Inventory[user_food] -= int(user_quantity)
	else:
		print("Please type 'add' or 'remove' to update the quantity of %s in Inventory" % user_food)
else :
	print("Sorry, there are no %s in Inventory" % user_food)

print(Inventory)


