# def times_ten(arg):
#     return arg * 10

# print(times_ten(10))


# value = 12
# result = times_ten(value)
# print(result)


# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)


# my_function(a=2, b=4, c=6)

# import random

# def main():
#     rand = random.randrange(1, 100)
#     print(rand)

# main()

# def half(number):
#     return number / 2

# # Пример использования функции
# number = 10.0  # Замените 10.0 на нужное вам значение
# result = half(number)
# print(result)  # Выведет 5.0, так как 10 / 2 = 5


# def cube(num):
    # return num * num * num
# 
# def main():
    # value = 4
    # result = cube(value)
    # print(result)
# 
# main()

# def main():
#     number = 5
#     res = times_ten(number)
#     print(res)
    

# def times_ten(value):
#     return value * 10
    

# main()


# #Me
# def get_first_name():
#     name = input("Enter your name: ")
#     return print(name)
    
# get_first_name()

# #GPT
# def get_first_name():
#     name = input("Enter your name: ")
#     return name

# user_name = get_first_name()
# print("Your name is:", user_name)



########  Упражнения по программированию  #########
# done
# def main():
#     print("\nWelcome to the Kilometer Converter!")
#     user_input = int(input("Enter the kilometers that you want to convert: "))
#     miles = convert(user_input)
#     print(f"\nMiles:{int(miles)}")

# def convert(kilom):
#     return kilom * 0.6214

# main()

#####     Me
# def get_the_cost():
#     price = int(input("How much the replacement cost? $"))
#     end = insurance(price)
    
#     print(f'The minimumamount of insurance is: ${end}')


# def insurance(prop_cost):
#     return 0.8 * prop_cost


# get_the_cost()

#################################3
# GPT
# def calculate_minimum_insurance():
#     try:
#         # Get the replacement cost from the user
#         replacement_cost = float(input("Enter the replacement cost of the building: $"))

#         # Calculate the minimum insurance amount (80% of replacement cost)
#         minimum_insurance = 0.8 * replacement_cost

#         # Display the result to the user
#         print(f"You should buy at least ${minimum_insurance:.2f} of insurance.")
#     except ValueError:
#         print("Invalid input. Please enter a valid replacement cost as a number.")

# if __name__ == "__main__":
#     calculate_minimum_insurance()




# 4. Automobile Cost


#### My version is fucking dreadful cuz it's done in a very inefficient way
#### too many lines of code. I could've done it in 11 lines of code!!!!!
#### SEE BELLOW

# def main():
#     print("Enter the monthly cost of the following expences:")

#     loan = loan_payment()
#     insurance = insurance_payment()
#     gas = gas_payment()
#     oil = oil_payment()
#     tires = tires_payment()
#     maintenance = maintenance_payment()

#     total_month = total_mon(loan, insurance, gas, oil, tires, maintenance)
#     total_annual = total_ann(loan, insurance, gas, oil, tires, maintenance)
#     print() 
#     print(f"Your total month expenses are: ${total_month:,.2f}")
#     print(f"Your total annual expenses are: ${total_annual:,.2f}")

# def loan_payment():

#     return float(input("Loan payment: "))

# def insurance_payment():
#     return float(input("Insurance payment: "))

# def gas_payment():
#     return float(input("Gas payment: "))

# def oil_payment():
#     return float(input("Oil payment: "))

# def tires_payment():
#     return float(input("Tires payment: "))

# def maintenance_payment():
#     return float(input("Maintenance payment: "))

# def total_mon(one, two, three, four, five, six):
#     return one + two + three + four + five + six

# def total_ann(one, two, three, four, five, six):
#     return (one + two + three + four + five + six) * 12

# main()




#### That's how CHATGPT has done it
# def calculate_expense_total():
#     # Get monthly expenses from the user
#     loan_payment = float(input("Enter monthly loan payment: $"))
#     insurance = float(input("Enter monthly insurance cost: $"))
#     gas = float(input("Enter monthly gas cost: $"))
#     oil = float(input("Enter monthly oil cost: $"))
#     tires = float(input("Enter monthly tire cost: $"))
#     maintenance = float(input("Enter monthly maintenance cost: $"))
#
#     # Calculate total monthly expenses
#     total_monthly_cost = loan_payment + insurance + gas + oil + tires + maintenance
#
#     # Calculate total annual expenses
#     total_annual_cost = total_monthly_cost * 12
#
#     # Display the results
#     print(f"Total monthly cost: ${total_monthly_cost:.2f}")
#     print(f"Total annual cost: ${total_annual_cost:.2f}")
#
# if __name__ == "__main__":
#     calculate_expense_total()
#     print('Hello world')


# 5. A Property Tax
# actual_price = float(input())
#
# assessment_value = 0.6 * actual_price
#
# property_tax = (assessment_value / 100) * 72
#
# print(f"Assessment Value: ${assessment_value:.2f}")
# print(f"Property Tax: ${property_tax:.2f}")



# 6. Calorits from Fat and Carbohydrates
# def get_input():
#     fat = float(input('Fat grams per day: '))
#     carbohydrates = float(input('Carbohydrate grams per day: '))
#     cal1, cal2 = convert_to_callories(fat, carbohydrates)
#     print(f"Calories from fat: {cal1}. Calories form carbs: {cal2}")

# def convert_to_callories(fat, carbohydrates):
#     calloriesFat = fat * 9
#     calloriesCarbo = carbohydrates * 4
#     return calloriesFat, calloriesCarbo

# get_input()


# 7. Stadium Seating

# print("How much tickets were sold for each class?")
# class1, class2, class3 = int(input("Class A: ")), int(input("Class B: ")), int(input("Class C: "))

# sales1 = class1 * 20
# sales2 = class2 * 15
# sales3 = class3 * 10

# total_sales = sales1 + sales2 + sales3

# print('Total sales: $', total_sales)




# 8. Paint Job Estimator

# Get input from user
# square_feet = float(input("Enter the square feet of wall space to be painted: "))
# paint_price = float(input("Enter the price of the paint per gallon: "))

# # Calculate gallons of paint required
# gallons_of_paint = square_feet / 112

# # Calculate hours of labor required
# hours_of_labor = gallons_of_paint * 8

# # Calculate cost of paint
# cost_of_paint = gallons_of_paint * paint_price

# # Calculate labor charges
# labor_charges = hours_of_labor * 35

# # Calculate total cost of paint job
# total_cost = cost_of_paint + labor_charges

# # Display results
# print("Gallons of paint required:", gallons_of_paint)
# print("Hours of labor required:", hours_of_labor)
# print("Cost of paint: $", cost_of_paint)
# print("Labor charges: $", labor_charges)
# print("Total cost of paint job: $", total_cost)



# 9. Monthly Sales Tax

# def main():
#     total_sales = float(input("Enter the total sales: "))
#     county_sales = 0.05 * total_sales
#     state_sales = 0.025 * total_sales
#     total_sales_tax = county_sales + state_sales

#     print(f"The amount of county sales tax: ${county_sales:,.2f}")
#     print(f"The amount of state sales tax: ${state_sales:,.2f}")
#     print(f"The total sales tax (county plus state): ${total_sales_tax:,.2f}")


# main()




# 10. Feet to Inches





