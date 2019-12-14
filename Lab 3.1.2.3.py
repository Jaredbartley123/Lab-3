#Lab 5

#Secret Number
secret_number = 42

#Displays the task and takes users input
userInput = int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""))

#If number is incorrect repeats question
while  userInput != secret_number:
    print("Ha ha! You're stuck in my loop!")
    userInput = int(input("Try again: "))

#If number is correct ends program
if userInput == secret_number:
    print("Well done, muggle! You are free now.")
    
    

