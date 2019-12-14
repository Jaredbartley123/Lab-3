#Lab 10

#takes input from user
blocks = int(input("Enter the number of blocks: "))

#defines initial requirements for pyramid
pyramid = 1
height = 0

#builds pyramid from top to bottom
while blocks >= pyramid:
    blocks = blocks - pyramid
    height = height + 1
    pyramid = pyramid + 1
    
#prints pyramid height
print("The height of the pyramid:", height)
