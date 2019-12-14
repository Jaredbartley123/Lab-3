#lab 4
#Takes Input from user and puts into year variable
year = int(input("Enter a year:"))

#Checks if number is valid 
if year < 1582:
    print('Not within the Gregorian calandar')

#Calculates if variable is a common or leap year
else:
    if year % 4 != 0:
        print('It\'s a Common Year')

    elif year % 100 != 0:
        print("It's a Leap Year")

    elif year % 400 != 0:
        print("It's a Common Year")

    else:
        print('It\'s a Leap Year')


    
