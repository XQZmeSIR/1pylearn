# Исключение— это ошибка, которая происходит во время работы программы,
# приво­дящая к ее внезапному останову.
# Для корректной обработки исключений
# используется инструкция try/except


    
# def main():
#  # Initialize an accumulator.
#     total = 0.0 
#     try:
#  # Open the sales_data.txt file.
#         infile = open('sales_data.txt', 'r')
#         # Read the values from the file and
#         # accumulate them.
#         for line in infile:
#             amount = float(line)
#             total += amount
#         # Close the file.
#         infile.close()
#         # Print the total.
#         print(f'{total:,.2f}')

# except IOError:
#     print('An error occured trying to read the file.')
# except ValueError:
#     print('Non-numeric data found in the file.')
# except:   #### Использование одного выражения except
#           #### для отлавливания всех исключений
#     print('An error occured.')

# # Call the main function.
# if __name__ == '__main__':
#     main()



def main():
    try:
        hours = int(input('Сколько часов вы отработали? '))
        pay_rate = float(input('Введите почасовую ставку: '))
        gross_pay = hours * pay_rate
    
        print(f'Зарплата: ${gross_pay:,.2f}')
    except ValueError as err:
        print(err)
    finally:
        print("""
        `Finally` group workes as a last chain in `try/except` sequence.
        It is being executed last.
        So the hierarchy is: `try` --> `except` --> `finally`.
        It is executed regargless if there is or not any Exceptions.
        """)

main()



#