bankAccount = 10000
interest = 0.5
collegeExpenses = 500
numOfMonth = 0
while bankAccount > 0:
    bankAccount = (bankAccount - collegeExpenses) * 1.005
    numOfMonth += 1
year = float(numOfMonth)/12
print(year)