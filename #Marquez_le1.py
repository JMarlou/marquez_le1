#Marquez_le1

import sys

game_library = {

    "Donkey Kong": {"quantity": 3, "cost": 2},

    "Super Mario Bros": {"quantity": 5, "cost": 3},

    "Tetris": {"quantity": 2, "cost": 1},

}

admin_username = "admin"
admin_password = "adminpass"

user_accounts = {}

def register_user():
	name = input("Enter username: ")
	password = input("Enter password: ")
	if name in user_accounts:
		print("Username already exists!")
		input()
		main()
	else:
		user_accounts[name] = {"name": name, "password": password, "balance" : 0, "inventory": {}, "points" : 3}
		print("Accounted Successfully Registered\n")
		main()
	
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    
    if username in user_accounts:
        if user_accounts[username]["password"] == password:
            print("Login successful!")
            logged_in_menu(username)
        else:
            print("Incorrect password\n")
            main()
    else:
        print("Username not found\n")
        main()
        
def display_games():
	for game, details in game_library.items():
	   print(f"{game}: Copies {details['quantity']} - ${details['cost']} ")
	
def rent_game(username):
	balance = user_accounts[username]["balance"]
	points = user_accounts[username]["points"]
	item_game = input("Choose a game to borrow: ")
	if item_game in game_library:
		if game_library[item_game]["quantity"] > 0:
		   game_price = game_library[item_game]["cost"]
		   print(f"Price of {item_game}: ${game_price} with {game_library[item_game]['quantity']} current copies.")
		   ans = input("Borrow it (Y or N): ")
		   if ans == 'Y':
		   	if balance >= game_price:
		   		balance -= game_price
		   		game_price /= 2
		   		if game_price <= 0.5:
		   			pass
		   		else:	
		   			points += 1
		   		game_library[item_game]["quantity"] -= 1
		   		user_accounts[username]["balance"] = balance
		   		user_accounts[username]["points"] = points
		   		user_accounts[username]["inventory"].setdefault(item_game, 0)
		   		user_accounts[username]["inventory"][item_game] +=1
		   		print(f"Borrowed 1 copy of {item_game}")
		   		print(f"Remaining Balance: ${balance}")
		   	else:
		   	     print(f"Insufficient Funds!")
		   else: 
		   	logged_in_menu(username)
		else:
			print("No more copies!")
	else:
		print("Game is not in Store!")    
	
def return_game(username):
	item_game = input("Choose a game to return: ")
	if item_game in game_library:
		if item_game in user_accounts[username]["inventory"]:
			user_accounts[username]["inventory"][item_game] -=1
			game_library[item_game]["quantity"] += 1
			print(f"Returned {item_game} successfully!")
		else:
			print("Game not in borrowed.")
	else:
		print("Game not in Store!")
		
def borrowed_games(username, inventory):
	print("===Borrowed Games:===")
	for game, quantity in inventory.items():
            print(f"{game}: {quantity}")
	
def top_up_account(username):
	amount = float(input("Enter Amount to topup: "))
	user_accounts[username]["balance"] += amount
	print("Successful TopUp!")
	
def redeem_free_rental(username):
	points = user_accounts[username]["points"]
	display_games()
	item_game = input("Enter Game to Redeem: ")
	if item_game in game_library:
		if game_library[item_game]["quantity"] > 0:
			if points >= 3:
				points -= 3
				game_library[item_game]["quantity"] -= 1
				user_accounts[username]["points"] = points
				user_accounts[username]["inventory"].setdefault(item_game, 0)
				user_accounts[username]["inventory"][item_game] +=1
				print(f"Successfully redeemed {item_game}!")
			else:
				print("Insufficient Points")
		else: 
			print("No More Copies Available!")
	else: 
		print("Game not in Store")

def logged_in_menu(username):
	balance = user_accounts[username]["balance"]
	inventory = user_accounts[username]["inventory"]
	points = user_accounts[username]["points"]
	print(f"Welcome {username}!, Current Balance: ${balance}, Points : {points}\n")
	print("===Rental Menu===")
	print("1. Display Games")
	print("2. Rent Game")
	print("3. Return Game")
	print("4. Borrowed Games")
	print("5. TopUp")
	print("6. Redeem Points")
	print("7. Log Out")
	print("8. Exit")
	
	choice = input("Choose Action: ")
	if choice == '1':
		display_games()
	elif choice == '2':
		rent_game(username)
	elif choice == '3':
		return_game(username)
	elif choice == '4':
		borrowed_games(username, inventory)
	elif choice == '5':
		top_up_account(username)
	elif choice == '6':
		redeem_free_rental(username)
	elif choice == '7':
		main()
	elif choice == '8':
		sys.exit()
	else:
		print("Invalid Action\n")
		logged_in_menu(username)
	input()
	logged_in_menu(username)


def check_admin(username, password):
	if username == "admin":
		if password == "adminpass":
			return True
		else:
			print("Wrong Password!")
			return False
	else:
		print("Wrong Username!")
		return False
			
def admin_login():
	print("Enter Credentials to Attain Admin Powers! ")
	username = input("Username: ")
	password = input("Password: ")
 	
	if check_admin(username, password):
		admin_menu()
	else:
		print("Get Out.\n")
		
def admin_update_game(game_library):
    print("=== Update Games ===")
    print("1. Add Game")
    print("2. Update Game Quantity")
    print("3. Update Game Price")
    print("4. Back to Admin Menu")
    
    choice = input("Action: ")
    if choice == '1':
        game_name = input("Enter the name of the game: ")
        if game_name in game_library:
            print("Game already in Inventory")
        else:
            quantity = int(input("Enter quantity of game: "))
            cost = float(input("Enter cost of the game: "))
            game_library[game_name] = {"quantity": quantity, "cost": cost}
            print("Successfully Added!")
    elif choice == '2':
        game_name = input("Enter the name of the game to add quantity: ")
        if game_name in game_library:
            new_quantity = int(input("Enter quantity to add to game: "))
            game_library[game_name]["quantity"] += new_quantity
            print(f"Quantity of {game_name} updated successfully!")
        else:
            print("Game not found in inventory.")
    elif choice == '3':
        game_name = input("Enter the name of the game to update price: ")
        if game_name in game_library:
            new_cost = float(input("Enter new cost of the game: "))
            game_library[game_name]["cost"] = new_cost
            print(f"Price of {game_name} updated successfully!")
        else:
            print("Game not found in inventory.")
    elif choice == '4':
        input()
        admin_menu()
    else:
        print("Invalid choice. Please try again.")
    input()
    admin_update_game(game_library)
    
def display_game_inventory():
	for game, details in game_library.items():
	   print(f"{game}: Copies {details['quantity']} - ${details['cost']} ")

def admin_menu():
	print("===Welcome Sire!===")
	print("1. Display Games")
	print("2. Update Games")
	print("3. Log Out")
	print("4. Exit")
	
	choice = input("Action: ")
	if choice == '1':
		display_game_inventory()
	elif choice == '2':
		admin_update_game(game_library)
	elif choice == '3':
		main()
	elif choice == '4':
		sys.exit()
	else:
		print("Invalid Input!\n")
	input()
	admin_menu()
			
def main():
	print("Enter Action:")
	print("1. Admin")
	print("2. Register")
	print("3. Login")
	print("4. Exit")
	
	choice = input("Choose what to do: ")
	if choice == '1':
		admin_login()
	elif choice == '2':
		register_user()
	elif choice == '3':
		login()
	elif choice == '4':
		sys.exit(0)
	else: 
		print("Invalid Input!")
		main()
	input()	
					
if __name__ == "__main__":

	main()
