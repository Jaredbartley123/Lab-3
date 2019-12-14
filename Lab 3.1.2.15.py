#lab 11

#takes input from user
num = int(input("Input a number: "))

count = 0

while num != 1:

#if number is odd 
    if num % 2 != 0:
        num = 3 * num + 1

#if number is even      
    elif num % 2 == 0:
        num = num / 2

#prints answer
    print(int(num))

#adds 1 to counter and repeats until down to 1
    count = count + 1

#prints the amount of steps required
print("Steps: " + str (count))


        
