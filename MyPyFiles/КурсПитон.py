# is_authorized = True
# print(is_authorized)
# print(type(is_authorized))
# print(bool(10))
# print(bool('sfv'))
# print(bool([1, 2]))
# print(bool(None))


# print('One', 'Two', 'Three', sep='---')

# print('One', 'Two', 'Three', end='!')


# print('''


# ''')





# # Escape Characters
# # Экранированные символы

# print("One\nTwo\nThree")

# # The \t escape character advances the output to the next horizontal tab position.
# print ('Пн\tВт\tCp')
# print ('Чт\tПт\tСб')


# # Use the \' and \" escape characters to display quotation marks.
# print("Your assignment is to read \"Hamlet\" by tomorrow.")
# print('I\'m ready to begin.')

# #  Use the \\ escape character to display a backslash,
# print("\nYour path to \\C is C:\\temp")


# # F-strings, or formatted string literals


val = 10 - 2 + 2429
print(f'The value is {val}')

# This program demonstrates how a floating-point
# number is displayed with no formatting.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'The monthly payment is {monthly_payment:.5f}.')

a = 2
b = 3
print(f"{a / b:.1f}")


# Inserting Comma Separators <,
















number = 1234567890.12345 
print(f"{number:,.2f}")

monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Your annual pay is ${annual_pay:,.2f}')


print('''




''')


# Formatting a Floating-Point Number as a Percentage
discount = 0.5
print(f'{discount:.0%}')


# 
number = 123456789 
print(f'{number:e}')
print(f'{number:.2e}') 


# // Formatting Integers.
# When you need to use a type designator, use d or D.
# This indicates that the value should be displayed
# as a decimal integer.
 
number = 123456
print(f'{number:,d}')


# // Specifying a Minimum Field Width
number = 99
print(f'The number is {number:5}')

# The following example displays a floating-point value
# rounded to 2 decimal places, with comma separators,
# in a field that is 12 spaces wide:
number = 12345.6789
print(f'The number is {number:12,.2f}')


print('''



''')



# Alignment Designators
#  < Left-aligns the value
#  > Right-aligns the value
#  ^ Center-aligns the value

number = 10
string = 'Hey'

print(f'{number:>20.2f}')

# This program demonstrates how to center-align strings.
name1 = 'Gordon'
name2 = 'Smith'
name3 = 'Washington'
name4 = 'Alvarado'
name5 = 'Livingston'
name6 = 'Jones'
name7 = 'Mike'
# Display the names.
print(f'***{name1:^20}***')
print(f'***{name2:^20}***')
print(f'***{name3:^20}***')
print(f'***{name4:^20}***')
print(f'***{name5:^20}***')
print(f'***{name6:^20}***')
print(f'***{name7:^20}***')


print('''

''')

# Concatenation with F-strings
name = 'Abbie Lloyd'
department = 'Sales'
position = 'Manager'
print(f'Employee Name: {name}, ' +
        f'Department: {department}, ' +
        f'Position: {position}')
# При конкатенации двух или более f-строк необходимо указывать отддельный f-префикс дл каждого строкового литерала.

int_num = 5
bool_val = True
print(bool_val + int_num)

lis = []
print(help(lis.__eq__))















