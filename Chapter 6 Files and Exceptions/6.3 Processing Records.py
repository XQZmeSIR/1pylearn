# def main():
#     num_emps = int(input("How many records do you want to create? "))

#     with open('employees.txt', 'w') as emp_file:
#         for count in range(1, num_emps + 1):
#             print(f'Enter data about employee #{count}')
#             name = input('Name: ')
#             id_num = (input('ID: '))
#             dept = input('Department: ')

#             emp_file.write(f'{name}\n')
#             emp_file.write(f'{id_num}\n')
#             emp_file.write(f'{dept}\n')
#             print()

#         emp_file.close()
#         print('Records have been saved in employees.txt')

# if __name__ == "__main__":
#     main()


# def main():
#     with open('employees.txt', 'r') as emp_file:
#         name = emp_file.readline()

#         while name != '':
#             id_num = emp_file.readline()
#             dept = emp_file.readline()

#             name = name.rstrip()
#             id_num = id_num.rstrip()
#             dept=dept.rstrip()

#             print(f"Name: {name}")
#             print(f'ID: {id_num}')
#             print(f'Department: {dept}')
#             print()
        
#             name = emp_file.readline()
#         emp_file.close()

# if __name__ == "__main__":
#     main()


# В центре внимания
# def main():
#     another = "y"

#     with open('coffee.txt', 'a') as coffee_file:
#         while another == 'y' or another == 'Y':
#             print('Enter the following coffee data:')
#             desc = input("Description: ")
#             qty = int(input('Quantity(in pounds): '))

#             coffee_file.write(desc + '\n')
#             coffee_file.write(f'{qty}\n')

#             print("Do you want to add another?")
#             another = input('Y = yes, anything else = no: ')
        
#         coffee_file.close()
#         print("Data appended to coffee.txt")

# if __name__ == "__main__":
#     main()


# def main():
#     found = False  # we need a flag for if

#     search = input("What do you want to find? ")

#     with open('coffee.txt', 'r') as coffee_file:
#         desc = coffee_file.readline()

#         while desc != '':
#             qty = float(coffee_file.readline())
#             desc = desc.rstrip('\n')

#             if desc == search:   # as usual but in a if condition
#                 print(f'Description: {desc}')
#                 print(f'Quantity: {qty}')
#                 print()

#                 found = True    # update flag to true

#             desc = coffee_file.readline()

#         if not found:       # use the flag in if not
#             print('This value cannot be found in a file.')

# if __name__ == "__main__":
#     main()


# Changing notes in file
# import os

# def main():
#     found = False

#     search = input('Enter the needed description: ')
#     new_qty = int(input("Enter the new quantity: "))

#     with open('coffee.txt', 'r') as coffee_file:
        
#         temp_file = open('temp.txt', 'w')
        
#         desc = coffee_file.readline()
    
#         while desc != '':
#             qty = float(coffee_file.readline())
#             desc = desc.rstrip()

#             if desc == search:
#                 temp_file.write(f'{desc}\n')
#                 temp_file.write(f'{new_qty}\n')
#                 found = True

#             else:
#                 temp_file.write(f'{desc}\n')
#                 temp_file.write(f'{qty}\n')

#             desc = coffee_file.readline()

#     os.remove('coffee.txt')
#     os.rename('temp.txt', 'coffee.txt')

#     if found:
#         print("File's updated")
#     else:
#         print("This value hasn't been found.")

# if __name__ == "__main__":
#     main()


import os

def main():
    found = False

    search = input('What coffee item do you want to delete? ')

    with open('coffee.txt', 'r') as coffee_file:
        
        temp_file = open('temp.txt', 'w')
        
        desc = coffee_file.readline()
    
        while desc != '':
            qty = float(coffee_file.readline())
            desc = desc.rstrip()

            if desc != search:
                temp_file.write(f'{desc}\n')
                temp_file.write(f'{qty}\n')
                
            else:
                found = True

            desc = coffee_file.readline()

    os.remove('coffee.txt')
    os.rename('temp.txt', 'coffee.txt')

    if found:
        print("File's updated")
    else:
        print("This value hasn't been found.")

if __name__ == "__main__":
    main()








#