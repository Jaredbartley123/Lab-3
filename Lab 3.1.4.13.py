#Lab 13

#creates empty list for beatles 
beatles = []

#prints empty list
print("Step 1: ", beatles)

#adds 3 names to list and prints them in order of top to bottom
beatles.append("John lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print('Step 2: ', beatles)

#asks user to input other band members and prints the members
for i in range (2):
    beatles.append(str(input('Enter new band member: ')))
print('Step 3:', beatles)

#removes band members recently added and prints the members 
del beatles[-2]
del beatles[-1]
print('Step 4: ', beatles)

#adds ringo starr to beginning of list and prints new roster
beatles.insert(0, 'Ringo Starr')
print('Step 5: ', beatles)

#prints the amount of members in the beatles 
print("The Fab: ", len(beatles))
