def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}', 'Category: {expense["category"]}')

expenses = []
test = lambda x: x * 2
list = [2,3,5,8]
index = 1
for element in list:
    print(index,": ",test(element))
    index+=1
print("Sum of square of list: ",sum(map(test, [2, 3, 5, 8])))