total=0
expenses = []
for i in range(7): 
    expenses.append(float(input("Enter your expense\n")))
total=sum(expenses)
print(total)