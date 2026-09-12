from expense import Expense

def main():
    print("Welcome to your expense tracker!")
    expense_file_path = "expenses.csv"
    
    #  Get expense and save it
    new_expense = get_user_expense()
    if new_expense:
        save_expense_to_file(new_expense, expense_file_path)
    
    # Summarise expenses
    summarise_expense(expense_file_path)

def get_user_expense():
    expense_name = input("Enter expense: ")
    
    try:
        expense_amount = float(input("Enter expense amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return None
        
    expense_category = [
    "Food", 
    "Housing", 
    "Utilities", 
    "Fun", 
    "Transportation"
    ]
    
    while True:
        print("Select a category:")
        for i, category_name in enumerate(expense_category):
            print(f" {i+1}. {category_name}")
            

        selected_index = int(input("Enter expense category (1-5): "))
            
        if selected_index in range(1, len(expense_category) + 1):
            selected_category = expense_category[selected_index - 1]
                
                
            print(f"Expense Added: {expense_name}, ${expense_amount:.2f} --> {selected_category}.\n")
                
            return Expense(name=expense_name, amount=expense_amount, category=selected_category)
        else:
            print("Please enter a valid number.")

def save_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense to file: {expense.name} to {expense_file_path}...")
    with open(expense_file_path, "a") as f:
        
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarise_expense(expense_file_path):
    print("\n--- Summarising User Expenses ---")
    expenses: list[Expense] = []

    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip():
                continue
                    
            expense_name, expense_amount, expense_category = line.strip().split(",")
                    
            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
            
        total_spent = sum([expense.amount for expense in expenses])
        
        print(f"Total Expenses: ${total_spent:.2f}")
    

if __name__ == "__main__":
    main()


