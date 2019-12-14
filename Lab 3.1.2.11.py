#Lab 9

#creates empty string for word without vowels to be stored
wordWithoutVowels = ""

#takes input from user
userWord = input("Please enter a word: ")

#makes all letters uppercase
userWord = userWord.upper()

#takes out all vowels 
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
        wordWithoutVowels += letter

#prints the final product
print(wordWithoutVowels)
