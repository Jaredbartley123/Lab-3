myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newList = []

for num in myList:
    if num not in newList:
        newList.append(num)

myList = newList

print("The list with unique elements only: ")
print(myList)
