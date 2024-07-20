import random

def roll():
    min_val = 1
    max_value = 6
    return random.randint(min_val, max_value)

# Get the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Enter a digit.")

# Get player names
player_name = []
for i in range(players):
    name = input(f"Enter player {i + 1} name: ")
    player_name.append(name)

max_score = 10
player_score = [0 for _ in range(players)]

# Main game loop
while max(player_score) < max_score:
    for i in range(players):
        print(f"Player {player_name[i]}'s turn has started!\n")
        print(f"Your current score is: {player_score[i]}\n")
        
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (yes/no)? ").lower()
            if should_roll != "yes":
                break
            
            value = roll()
            if value == 1:
                print("You rolled 1! Turn done!\n")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your score this turn is: {current_score}")

        player_score[i] += current_score
        print(f"Your total score is: {player_score[i]}\n")
# Determine the winner
max_score = max(player_score)
player_winning = player_score.index(max_score)
print(f"Player {player_name[player_winning]} won with a score of: {max_score}")
