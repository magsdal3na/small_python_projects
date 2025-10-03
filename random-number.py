import random

randNum = random.randint(1, 1000);
print(randNum)

guess = -1

print("It's guessing game time!")
print("To start, please enter a\nnumber into the input box.\n")
print("The module will tell you\nif you are close to the\nnumber or not.\n")
print("The number is between\n1 and 1000.\n")
print("Let's get started!\n")

while guess != randNum:
  try:
    user_input = input("Please enter your guess: ")
    guess = int(user_input)
  except ValueError:
    print("Must be a valid number. Please try again.")
    continue
  
  if(guess < randNum):
    print("Too low. Try again!\n")
  elif (guess > randNum):
    print("Too high. Try again!\n")
  elif (guess == randNum):
    print(f"You got it! The number was {randNum}.")
    break
