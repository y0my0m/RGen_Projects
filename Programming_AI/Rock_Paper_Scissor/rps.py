from random import randint

choices = ["rock", "paper", "scissors"]

computer_choice = choices[randint(0, 2)]
player_choice = False

while player_choice == False:
    print("Press 'q' to Quit!")
    player_choice = input("\nChoose your option Rock, Paper or Scissor : ")
    player_choice = player_choice.lower().strip()
    if player_choice == "q":
        player_choice = True
        continue
    if player_choice not in choices:
        print("invalid input, try again")
        player_choice = False
        continue
    elif player_choice == computer_choice:
        print("It's a tie! Both players selected", player_choice)
    elif player_choice == "rock":
        if computer_choice == "scissors":
            print("You win! Rock beats Scissors")
        else:
            print("You lose! Paper beats Rock")
    elif player_choice == "scissors":
        if computer_choice == "paper":
            print("You win! Scissors beats Paper")
        else:
            print("You lose! Rock beats Scissors")
            
    elif player_choice == "paper":
        if computer_choice == "rock":
            print("You win! Rock beats Scissors")
            print("You win! Scissors beats Paper")
        else:
            print("You lose! Paper beats Rock")
            
    player_choice = False