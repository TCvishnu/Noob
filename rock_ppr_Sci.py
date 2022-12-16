import random as r


class Objects:
    def __init__(self, letter_of_weapon: str, name: str):
        self.name = name
        self.letter_of_weapon = letter_of_weapon
        self.weapon_list = {'r': 'Rock', 'p': 'Paper', 's': 'Scissor', 'n': 'None'}
        ''' None is not a choice in-game, but given for object instantiation'''

        self.weapon = self.weapon_list[self.letter_of_weapon]

    def weapon_choose_display(self):
        print(f"{self.name} chose {self.weapon}")

    def point_winner_display(self):
        print(f"{self.name} won a point!!")


class Menu:
    def __init__(self):
        print("MENU:")
        print("r:Rock")
        print("p:Paper")
        print("s:Scissor")
        self.choice = input("Enter Your Choice: ").lower()

    def return_choice(self):
        return self.choice


class Score:
    def __init__(self, name: str):
        self.name = name  # display purpose
        self.score = 0

    def increment_score(self):
        self.score += 1


def print___():
    print("=" * 20)
    print("=" * 20)


# Player objects
user = Objects('n', 'You')  # letter_of_weapon given as n for first instantiation purpose
computer = Objects('n', 'Computer')
play_again = 'y'

while play_again == 'y':
    print___()
    print("Rock Paper Scissors!!")
    rounds = int(input("Enter the number of rounds you want to play: "))
    print___()

    user_score = Score('Your')
    computer_score = Score("Computer's")

    for i in range(1, rounds + 1):
        print(f"Round {i}/{rounds + 1}")
        menu_display = Menu()
        cmp_chose_weapon_letter = r.choice(["r", "p", "s"])

        # re-creating objects based on Choices: Rock, Paper or Scissor
        user = Objects(menu_display.return_choice(), 'You')
        computer = Objects(cmp_chose_weapon_letter, 'Computer')

        print___()

        if computer.weapon == 'Rock':
            if user.weapon == 'Paper':
                user_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                user.point_winner_display()

            elif user.weapon == 'Scissor':
                computer_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                computer.point_winner_display()
            else:
                user.weapon_choose_display()
                computer.weapon_choose_display()
                print("Both Chose Same, No Points")

        elif computer.weapon == 'Paper':
            if user.weapon == 'Scissor':
                user_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                user.point_winner_display()

            elif user.weapon == 'Rock':
                computer_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                computer.point_winner_display()
            else:
                user.weapon_choose_display()
                computer.weapon_choose_display()
                print("Both Chose Same, No Points")

        elif computer.weapon == 'Scissor':
            if user.weapon == 'Rock':
                user_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                user.point_winner_display()

            elif user.weapon == 'Paper':
                computer_score.increment_score()
                user.weapon_choose_display()
                computer.weapon_choose_display()
                computer.point_winner_display()
            else:
                user.weapon_choose_display()
                computer.weapon_choose_display()
                print("Both Chose Same, No Points")

        print___()
        print("Scores:")
        print(f"You: {user_score.score}")
        print(f"Computer: {computer_score.score}")
        print___()
    else:
        if user_score.score > computer_score.score:
            print(f"You Won the Game!!!")
        elif user_score.score < computer_score.score:
            print(f"Computer won the game!!")
        else:
            print("Game tied!!")

    play_again = input("Do You Want to Play Again?\nPress y to play (or) any other key to exit: ")
