# Expense Tracker Project

expensesList = []  # list of expenses in form of dictionary
print("Welcome to Expense Tracker: Kharcha kam kiya karo")

while True: 
    print("===== MENU =====")
    print("1. Add Expense") 
    print("2. View All Expenses")     
    print("3. View Total Kharcha")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))

    # 1. ADD Expense
    if choice == 1:
        date = input("Kis date par kharcha kiya tha? ")
        category = input("Kis type ka kharcha kiya? (Food, Travel, Makeup, Books) ")
        description = input("Aur detail dedo: ")
        amount = float(input("Enter the amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\nDone Bro. Expense is added successfully")

    # 2. VIEW ALL EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added. Jao Pehle Kharcha Karo.")
        else:
            print("==== Ye hai apka sara expense ====")
            count = 1
            for eachKharcha in expensesList:
                print(f"Kharcha Number {count} -> {eachKharcha['date']}, {eachKharcha['category']}, {eachKharcha['description']}, {eachKharcha['amount']}")
                count += 1

    # 3. View Total Spending    
    elif choice == 3:
        total = 0
        for eachKharcha in expensesList:
            total += eachKharcha["amount"]

        print("\nTOTAL KHARCHA = ", total)

    # 4. EXIT 
    elif choice == 4:
        print("Dhanyawad aapne humara system use kiya")
        break   # <-- while True লুপ থেকে বের হয়ে যাবে

    else:
        print("INVALID CHOICE. TRY AGAIN")
