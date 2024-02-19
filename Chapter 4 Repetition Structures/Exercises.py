# while True:
#     # Prompt the user to enter two numbers
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     # Calculate the sum
#     sum_result = num1 + num2
    
#     # Display the sum
#     print(f"The sum of {num1} and {num2} is {sum_result}")
    
#     # Ask if the user wants to perform the operation again
#     repeat = input("Do you want to perform the operation again? (yes/no): ").lower()
    
#     if repeat != "yes":
#         break  # Exit the loop if the user's input is not "yes"

# for tens in range(0, 1001, 10):
#     print(tens)


# # Initialize a variable to store the running total
# total = 0

# # Use a for loop to iterate 10 times
# for i in range(10):
#     # Ask the user to enter a number
#     num = float(input("Enter a number: "))
    
#     # Add the entered number to the running total
#     total += num

# # Print the final total
# print("The sum of the 10 numbers is:", total)



# for i in range(10):  # Loop for 10 rows
#     for j in range(15):  # Loop for 15 characters in each row
#         print("#", end="")
#     print()  # Move to the next line after printing 15 '#' characters



# 8. Write code that prompts the user to enter a positive nonzero number and validates
# the input.
# 9. Write code that prompts the user to enter a number in the range of 1 through 100 and
# validates the input.

# while True:
#     try:
#         # Ask the user for input
#         user_input = input("Enter a positive, nonzero number: ")

#         # Convert the user's input to a floating-point number
#         number = float(user_input)

#         # Check if the number is positive and nonzero
#         if number > 0:
#             break  # Exit the loop if the input is valid
#         else:
#             print("Please enter a positive, nonzero number.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# # You now have a valid positive, nonzero number in the 'number' variable.
# print("You entered:", number)


# while True:
#     try:
#         user_input = input('Enter a number between 1 and 100: ') # input
#         number = int(user_input) # Conver to integer

#         if 1 <= number <= 100: # condition according to uslovie
#             break  # break if all data is correct
#         else:  # else if we enter a number out of range
#             print("Please enter a number between 1 and 100.")
#     except ValueError: ## except if we enter invalid data for instance some character
#         print('Invalid input. Please enter a valid number.')
# print('Your number is', number) ## if all correct this will be printed after if and break



# 1. Bug Collector

# total = 0

# for i in range(5):
#     day = i + 1  # Increment day by 1 
#     print(f'Day {day}')
#     bug = int(input('How much bugs have you collected today? '))
#     total += bug
# print('Your total number of bugs is', total)



# 2. Calories Burned

# PER = 4.2

# for i in range(10, 30, 5):
#     burned = i * PER
#     print(f"After {i} minutes you've burned {burned} callories.")



# 3. Budget Analysis

# Ask the user for the budget amount
budget = float(input("Enter your budget for the month: "))

# Initialize a variable to keep track of total expenses
total_expenses = 0.0

# Ask the user to enter expenses until they want to stop
while True:
    expense = input("Enter an expense (or 'done' to finish): ")

    # Check if the user wants to stop entering expenses
    if expense.lower() == 'done':
        break

    # Convert the entered expense to a float
    try:
        expense_amount = float(expense)
    except ValueError:
        print("Invalid input. Please enter a valid expense amount.")
        continue  # Skip the rest of the loop for this iteration

    # Add the expense to the total
    total_expenses += expense_amount

# Calculate the difference between the budget and total expenses
difference = budget - total_expenses

# Determine whether the user is over or under budget
if difference > 0:
    print(f"You are under budget by ${difference:.2f}.")
elif difference < 0:
    print(f"You are over budget by ${-difference:.2f}.")
else:
    print("You have spent your entire budget.")

