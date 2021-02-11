# Get the loan details from the user
money_owed=float(input("How much money do you owe?\n"))
apr = float(input("What is the yearly percentage rate?\n"))
monthly = float(input("What is the monthly payment amount?\n"))
months = int(input("How many months do you want to see the results for?\n"))

monthlyapr = apr/1200

for i in range(months):
    interestpermonth = monthlyapr*money_owed
    money_owed = money_owed + interestpermonth
    money_owed = money_owed - monthly


print("Money owed is",money_owed)