@@ -1,19 +1,19 @@
import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1-Rock, 2-Paper, 3-Scissors): ") # 1, 2, 3

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3!")
else:
    computerChoice = random.randint(1, 3)

    playerChoiceIndex = choices[playerChoice - 1] # ==> 0, 1, 2
    computerChoiceIndex = choices[computerChoice - 1]
    print(playerChoiceIndex,  computerChoiceIndex)
#    playerChoiceIndex = choices[playerChoice - 1] # ==> 0, 1, 2
#    computerChoiceIndex = choices[computerChoice - 1]
#    print(playerChoiceIndex,  computerChoiceIndex)

    # Determine the winner logic using if/elif/else
    if playerChoice == computerChoice:
@@ -25,4 +25,4 @@
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beats Paper - You win!")     
    else:
        print("You lose!")   
        print("You lose!")   
