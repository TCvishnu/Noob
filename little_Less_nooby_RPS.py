import random 

# Weapon Classes

class Rock:
	weapon_name = "Rock"

	def can_kill(self):
		return "Scissor"


class Paper:
	weapon_name = "Paper"

	def can_kill(self):
		return "Rock"


class Scissor:
	weapon_name = "Scissor"

	def can_kill(self):
		return "Paper"

# Player classes

class User:

	name = "You"
	points = 0

	def weapon_choosing(self):
		print("Choose: \nr:Rock\np:Paper\ns:Scissor")
		usr_choice = input().lower()

		if usr_choice == 'r':
			self.weapon = Rock()
		elif usr_choice == 'p':
			self.weapon = Paper()
		elif usr_choice == 's':
			self.weapon = Scissor()
		else:
			print20_()
			print("Invalid Input / Weapon!!")
			self.weapon_choosing()

		print20_()
		

class Computer:

	name = "Computer"
	points = 0

	def weapon_choosing(self):
		cmp_choice = random.choice(['r', 'p', 's'])
		
		if cmp_choice == 'r':
			self.weapon = Rock()
		elif cmp_choice == 'p':
			self.weapon = Paper()
		else:
			self.weapon = Scissor()

		print(f"{self.name} chose: {self.weapon.weapon_name}")
		print20_()


def print20_(): # Beautification
	print("_" * 20)


def play_game(usr, cmptr, current_round):

	if (current_round == 4) or usr.points == 2 or cmptr.points == 2: # Max Rounds = 3, so at 2 points, one of the players already won
		print("Game Over!")
		print20_()
		winner(usr, cmptr) # Funcition definition at line 121
		print20_()

		play_once_more = input("Enter Y to play again OR any other key to exit: ").upper()
		if play_once_more == 'Y':
			play_again(usr, cmptr) # Function def at line 131.
		else:
			print("Thank You for Playing : )")
			return

	else:
		print20_()
		print(f"Round: {current_round}")
		print20_()

		usr.weapon_choosing()
		print(f"{usr.name} chose: {usr.weapon.weapon_name}")

		cmptr.weapon_choosing()

		if usr.weapon.can_kill() == cmptr.weapon.weapon_name:
			print("You won a point!")
			usr.points += 1
		elif cmptr.weapon.can_kill() == usr.weapon.weapon_name:
			print("Computer won a point!")
			cmptr.points += 1
		else:
			print("Both chose same...Tie!")


		print20_()
		print_scores(usr, cmptr) # Function definition at line 115
		

		play_game(usr, cmptr, current_round + 1)


def print_scores(usr, cmptr):
	print("Scores:")
	print(f"User: {usr.points}")
	print(f"Computer: {cmptr.points}")


def winner(usr, cmptr): # To check who won User or Computer

	if usr.points > cmptr.points or usr.points == 2:
		print(f"{usr.name} Won!")
	elif usr.points < cmptr.points or cmptr.points == 2:
		print(f"{cmptr.name} Won!")
	else:
		print("Match Drawn")


def play_again(usr, cmptr):
	# New Game, so scores back to 0
	usr.points = 0
	cmptr.points = 0
	play_game(usr, cmptr, round_num)


# -------------------------------------------------------------------------------------------
user = User() # Class def at line 27
computer = Computer() # Class def at line 50
round_num = 1


print20_()
print("Game Starts!")

play_game(user, computer, round_num)
