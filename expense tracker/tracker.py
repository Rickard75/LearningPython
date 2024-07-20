'''An expenses tracker program that allows users to add expenses, list all expenses, show total expenses, and filter expenses by category'''

def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}', f'Category: {expense["category"]}')

def total_expenses(expenses):
    get_amount = lambda expense: expense['amount'] # amount is the cost of an expense
    return sum(map(get_amount,expenses))

def filter_expenses_by_category(expenses, category):
    my_lambda = lambda expense: expense['category'] == category
    return filter(my_lambda,expenses) # filter elements of iterable basing on a filter function
    

def main():
    # creatopn of expenses list
    expenses = []
    
    # testing lambda function
    test = lambda x: x * 2
    list = [2,3,5,8]
    index = 1
    for element in list:
        print(index,": ",test(element))
        index+=1
    print("Sum of square of list: ",sum(map(test, [2, 3, 5, 8])))
    
    # Menu
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print(f'\nTotal Expenses: {total_expenses(expenses)}')
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break
        
main()