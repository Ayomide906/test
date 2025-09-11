expense_list = [2340, 2500, 2100, 3100, 2980]
months=["JAN","FEB","MAR","APR","MAY"]
my_expense=int(input("Enter the expense: "))
for i in range(5):
    if my_expense==expense_list[i]:
        month=months[i]
        break
    else:
        month="none"
if month in months:
    print("You spent",my_expense, "in",month)
else:
    print("not found")



