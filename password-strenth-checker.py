import string

def contains_symbol_string_module(userInput):
  for char in userInput:
      if char in string.punctuation:
          return True
  return False

def check_mixed_case(userInput):
  #check for at least one uppercase and one lowercase character
  hasLower = any(char.islower() for char in userInput)
  hasUpper = any(char.isupper() for char in userInput)
  return hasLower and hasUpper

print("Welcome to the password strength checker!\n")
print("To start, please enter a possible password into the box.")
print("If your password meets the requirements, it will pass.")
print("If not, it will fail and you will have to try again.\n")

print("These are the requirements:")
print("1. Length must be equal to or more than 8 characters.")
print("2. At least one of the characters must be a number.")
print("3. At least one symbol must be included.")
print("4. At least one capital letter and one lowercase letter must be included.\n")

#parameters to check against
while True:

  #user input
  userInput = input()
  hasNumber = any(char.isdigit() for char in userInput)
  symbolCheck = contains_symbol_string_module(userInput)
  hasMixedCase = check_mixed_case(userInput)

  #checking if parameters are met
  if len(userInput) >= 8 and hasNumber == True and symbolCheck == True and hasMixedCase == True:
    print("Your password meets the requirements.")
    break
  elif len(userInput) <=7 or hasNumber == False or symbolCheck == False or hasMixedCase == False:
    print("Your password does not fulfill the requirements. Please try again.")
    continue  
  else:
    print("That is not valid. Try again.")
    continue
