import random

# List of monsters (name, health, attack power) nested list
monsters = [
    ["Dragon", 115, 15],
    ['Goblin',85,35],
    ['Mutant',110,25],
    ['Monster Obo',150,75]
    
  #add more lists containing monsters
]

print("Welcome to Monster Battle Arena!")

# Display available monsters
print("\nAvailable Monsters:")
for i in range(len(monsters)):
    print(f"{i + 1}. {monsters[i][0]} (Health: {monsters[i][1]}, Attack: {monsters[i][2]})") 

# Player chooses a monster
choice = int(input("\nChoose your monster by number: ")) - 1
player = monsters[choice]  # Assign the chosen monster to the player
print(f"\nYou chose: {player[0]}!")

# Randomly select an opponent
opponent = random.choice(monsters)
while opponent == player:  # Ensure the opponent is not the player's monster
    opponent = random.choice(monsters)

print(f"Your opponent is: {opponent[0]}!")

# Start the battle
while player[1] > 0 and opponent[1] > 0: #Game loop runs until one dies
    print("\nWhat would you like to do?")
    print("1. Attack")
    print("2. Defend")

    action = int(input("Enter 1 for Attack or 2 for Defend: "))

    if action == 1:  # Attack
        #What should happen here?
        print(f"\n{player[0]} attacks {opponent[0]} for {player[2]} damage!")
        opponent[1]=opponent[1] - player[2]
        if opponent[1]  <0 :
            opponent[1] = 0
        print(f"{opponent[0]}'s Health: {opponent[1]}")
    elif action == 2:  # Defend
        print(f"\n{player[0]} defends")
        player[1]=player[1]+5
        print(f"\n{player[0]}'s Health:{player[1]}")
          #What should happen here?

    if opponent[1] == 0:
        print (f"\n{player[0]} Won !!!")
        #Print Player wins 
        break  

    # Opponent's turn: Randomly decide to attack or defend
    opponent_action = random.choice([1, 2])  # 1 for attack, 2 for defend

    if opponent_action == 1:
        # Opponent attacks
        #What should happen here?
        print(f"\n{opponent[0]} attacks {player[0]} for {opponent[2]} damage!")
        player[1]=player[1] - opponent[2]
        if player[1]  <0 :
            player[1] = 0

    elif opponent_action == 2:  # Opponent defends
        #What should happen here?
        print(f"\n{opponent[0]} defends")
        opponent[1]= opponent[1]+5
        print(f"\n{opponent[0]}'s Health:{opponent[1]}")

    if player[1] == 0:
        print(f"\n{opponent[0]} Won !!!")
        #Print Opponent wins
        break

print("\nGame Over. Thanks for playing!")


