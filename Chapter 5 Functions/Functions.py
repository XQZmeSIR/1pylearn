# def message():  # Here we defined a function
#     print("I am Arthur")
#     print("the king of England!")

# message()   # and here we call the function

# def main():
#     print('i have a message')
#     message()
#     print('gppd biy')


# def message():
#     print("I am Arthur")
#     print("the king of England!")

# main()

# ### Передача аргумента в функцию
# def main():
#     intro()
#     cups_needed = int(input('Enter the number of cups: '))
#     cups_to_ounces(cups_needed) # инпут передается в параметр и затем в функц


# def intro():
#     print('This programm will help you to convert cups to ounces.')
#     print()


# def cups_to_ounces(cups):  #тут же функция принимает данные из мейна
#                            # и присваивает их (cups)
#     ounces = cups * 8
#     print(f'The entered number of cups will be {ounces} in ounces.')

# main()



# Передача нескольких аргументов

# def main():
#     first_name = input('Name: ')
#     second_name = input('Surname: ')
#     reverse_name(first_name, second_name)  # передаем параметры

# def reverse_name(name1, name2):
#     print(name1, name2)

# main()


########## Именованный аргумент  имя_анг=значение

# def main():
#     show_interest(rate=0.01, periods=10, principal=534000.0) # можно и цифры и строки

# def show_interest(principal, rate, periods):
#     interest = principal * rate * periods
#     print(interest)

# main()


CONTRBUTION_RATE = 0.05  # Gloval constanta

def main():
    gross_pay = float(input('Enter ur salary: '))
    bonus = float(input('Enter the sum of premii: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

def show_pay_contrib(gross):
    contrib = gross * CONTRBUTION_RATE
    print(f'Взнос из зп: ${contrib:,.2f}.')

def show_bonus_contrib(bonus):
    contrib = bonus*CONTRBUTION_RATE
    print(f'Взнос из прем: ${contrib:,.2f}.')
    

main()

