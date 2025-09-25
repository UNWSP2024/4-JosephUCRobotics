# Author: Joseph Kracht
# Last Modified: 9/23/2025
# Title: Average Rainfall

# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    # Initialise variables
    total_amount_of_rain = 0

    # Ask for the number of years.
    number_of_years = int(input("Input the number of years: "))

    # Loop through each year
    for year in range(number_of_years):
        # Loop through each month
        for month in range(12):
            # Add this month's rain to the total rain
            amount_of_rain = float(input("Input the amount it rained in year " + str(year + 1) + ", month " + str(month + 1) + ":"))
            total_amount_of_rain += amount_of_rain

    # Calculate the total number of months
    number_of_months = number_of_years * 12

    # Display the number of months, total rain, and the average amount of rain per month
    print("The total number of months is", number_of_months)
    print("The total amount of rain was", format(total_amount_of_rain, '.2f'))
    print("The average amount of rain per month is", format(total_amount_of_rain/number_of_months, '.2f'))

if __name__ == '__main__':
    main()
