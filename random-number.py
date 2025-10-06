import random

#initializing win variables
computerWin = 0
playerWin = 0
#setting up parameters for options and choice randomization
optionsList = ['rock', 'paper', 'scissors']

#display computer choice temporarily for debugging
print(randomChoice)

while playerWin < 3 and computerWin < 3:

  randomChoice = random.choice(optionsList)

  while True:
      userInput = input("What do you choose? Rock, Paper, or Scissors?").strip().lower()
      if userInput in optionsList:
        playerChoice = userInput
        break
      else:
        print("That is not a valid choice. Try again.")
        continue

  #choice comparisons and outcomes
  if playerChoice == randomChoice:
    print("You chose: " + playerChoice)
    print("Computer chose: " + randomChoice)
    print("That's a tie!")
  elif (playerChoice == "rock" and randomChoice == "scissors") or \
         (playerChoice == "paper" and randomChoice == "rock") or \
         (playerChoice == "scissors" and randomChoice == "paper"):
    print("You chose: " + playerChoice)
    print("Computer chose: " + randomChoice)
    print("Player +1")
    playerWin += 1
  else:
    print("Computer +1")
    computerWin += 1

  print(f"\nSCORE: Player {playerWin} - Computer {computerWin}")
if playerWin == 3:
  print("-" * 20)
  print("Player wins!")
elif computerWin == 3:
  print("Computer wins!")

