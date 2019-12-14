#lab 8

#takes input from user
userWord = input("Please enter a word: ")
#makes all letters uppercase
userWord = userWord.upper()

#takes out all vowels and prints remaining letters
for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
        
