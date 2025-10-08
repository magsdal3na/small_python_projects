import string

def contains_symbol_string_module(userInput):
  for char in userInput:
      if char in string.punctuation:
          return True
  return False

#parameters to check against
while True:

  #user input
  userInput = input()
  hasNumber = any(char.isdigit() for char in userInput)
  symbolCheck = contains_symbol_string_module(userInput)

  #checking if parameters are met
  if len(userInput) == 8 and hasNumber == True and symbolCheck == True:
    print("You have the bare minimum length required.")
    print("Your password contains numbers.")
    print("Your password contains symbols.")
    break
  elif len(userInput) == 8 and (hasNumber == False or symbolCheck == False):
    print("You have the bare minimum length required.")
    print("Your password does not contain numbers. Please try again.")
    continue  
  elif len(userInput) >= 9 and hasNumber == True and symbolCheck == True:
    print("Your password length is strong.")
    print("Your password contains numbers.")
    print("Your password contains symbols.")
    break
  elif len(userInput) >= 9 and hasNumber == False:
    print("Your password length is strong.")
    print("Your password does not contain numbers. Please try again.")
    continue
  elif len(userInput) <= 7:
    print("Your password length is weak. Please try again.")
    continue
  else:
    print("That is not valid. Try again.")
    continue

  #symbols(y/n)
  #uppercase included(y/n)
  #lowercase included(y/n)
