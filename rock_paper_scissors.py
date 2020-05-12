#rockpaperscissors

import random

# Define options
options = ["rock", "paper", "scissors"]
rock = options[0]
paper = options[1]
scissors = options[2]

# Define win conditions
winConditions = [
    [rock, scissors], #rock beat scissor,
    [paper, rock], #paper beat rock,
    [scissors, paper] #scissors beat paper
]

# Define lose conditions
loseConditions = [
    [scissors, rock],
    [rock, paper],
    [paper, scissors]
]

# Game loop

# Init vars
number_of_games = 0
num_of_wins = 0

while number_of_games < 3:
    # Get user input
    user = input("rock, paper or scissors? :  ")

    # Pick a random index
    random_index = random.randint(0, 2)

    # Compute response to random index
    choice = options[random_index]
    print(choice)

    # Check if you won/lose/draw
    game_state = [user, choice]
    if game_state in winConditions:
        print("Won!")
        # Increment number of wins
        num_of_wins += 1
    elif game_state in loseConditions:
        print("You lose!")
    else:
        print("Draw!")

    # Increment number of games
    number_of_games += 1

# Check if you won overall
if num_of_wins >= 2:
    print ("You won overall")

print("GAME OVER!")