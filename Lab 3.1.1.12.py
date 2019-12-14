#lab 3

income = float(input("Enter the annual income: "))

if income > 85828.00:
    tax = 14839.02 + ((income - 85528.00) * 0.32)
    print(float(totalIncome))

else:
    tax = (income * .18) - 556.02
   
tax = round(tax, 0)
if tax <= 0.0:
    tax = 0.0
    
print("The tax is:", tax, "thalers")
