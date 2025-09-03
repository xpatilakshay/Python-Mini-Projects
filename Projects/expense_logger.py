'''

📍 Concepts: File I/O, Read/Write/Append, CSV, JSON, Exception Handling.
📝 Task: Expense Logger

Add expenses (date, category, amount) → store in expenses.csv.

Read expenses → calculate total.

Export data to JSON.

Handle missing file errors with try/except.

'''

import csv

#csv_file = input("Enter the csv file name : ")
csv_file = "expenses.csv"
#json_file = input("Enter the json file name")
json_file = "expenses.json"

def add_expense(date,category, amount):
    try:
        with open("expenses.csv","a",newline="") as file:
            writer = csv.writer()
            writer.writerow([date,category, amount])
        print(f"Expense added {date} {category} {amount}")
    except Exception as e:
        print("Error while writting to file ",e)

def read_expenses():
    total = 0
    expenses = []
    try:
        with open("expenses.csv","r") as file:
            reader = csv.reader(file)
            for row in reader:
                date, category, amount = row
                total += amount
                expenses.append({"date":date,"category":category,"amount":amount})
            print("Total Expenses : ",total)
            return expenses
