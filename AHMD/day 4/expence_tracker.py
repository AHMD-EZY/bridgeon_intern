import json
from datetime import datetime
from pydantic import BaseModel, ValidationError


class ExpenseModel(BaseModel):
    category: str
    amount: float


def log_call(func) -> callable:
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as l:
            l.write(
                f"{datetime.now()} | Function: {func.__name__} | Args: {args}\n"
            )
        return func(*args, **kwargs)
    return wrapper


def load_file() -> list:
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses: list) -> None:
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)


@log_call
def add_expense(category: str, amount: float) -> None:
    try:
        expense = ExpenseModel(
            category=category,
            amount=amount
        )

        expenses = load_file()
        expenses.append(expense.model_dump())

        save_expenses(expenses)

        print("Expense Added Successfully!")

    except ValidationError as e:
        print("\nValidation Error:")
        print(e)


@log_call
def view_expenses() -> None:
    expenses = load_file()

    if not expenses:
        print("No expenses found.")
        return

    print("\nAll Expenses:")
    for expense in expenses:
        print(
            f"Category: {expense['category']} | Amount: {expense['amount']}"
        )


@log_call
def get_summary() -> None:
    expenses = load_file()
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    print("\nExpense Summary:")
    for category, amount in summary.items():
        print(f"{category}: {amount}")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Get Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))
            add_expense(category, amount)

        except ValueError:
            print("Amount must be a number!")

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        get_summary()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")