# Author: Joseph Kracht
# Last Modified: 9/23/2025
# Title: Bank Balance

# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    # Initialise variables
    total_expenses = 0.0

    # Get budget
    budget = float(input("Input your months budget: "))

    # Loop until 0 is entered
    while True:
        # Get an expense
        expense = float(input("Enter an expense or enter 0 to exit: "))
        if expense == 0:
            break
        total_expenses += expense

    # Get the amount over budget
    difference = total_expenses-budget

    # Display the result
    if difference >= 0:
        print("You are $", format(difference, '.2f'), "over budget")
    else:
        print("You are $", format(-difference, '.2f'), "under budget")


if __name__ == '__main__':
    main()
