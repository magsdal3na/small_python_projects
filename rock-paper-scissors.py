import random

#initializing win variables
computerWin = 0
playerWin = 0
#setting up parameters for options and choice randomization
optionsList = ['rock', 'paper', 'scissors']
randomChoice = random.choice(optionsList)
#display computer choice temporarily for debugging
print(randomChoice)

#player can input their choice
playerChoice = input()
print("You chose: " + playerChoice)

#choice comparisons and outcomes
if playerChoice == randomChoice:
  print("That's a tie!")
elif playerChoice == "rock" and randomChoice == "paper":
  print("Computer +1")
  computerWin += 1
  print(computerWin)
elif playerChoice == "rock" and randomChoice == "scissors":
  print("Player +1")
  playerWin += 1
elif playerChoice == "paper" and randomChoice == "rock":
  print("Player +1")
  playerWin += 1
elif playerChoice == "paper" and randomChoice == "scissors":
  print("Computer +1")
  computerWin += 1
elif playerChoice == "scissors" and randomChoice == "rock":
  print("Computer +1")
  computerWin += 1
elif playerChoice == "scissors" and randomChoice == "paper":
  print("Player +1")
  playerWin += 1
  

