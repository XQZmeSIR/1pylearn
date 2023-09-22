# height = int(input("Введите свой рост: "))
# print(height)

# color = input("Type your fav color: ")
# print(color)

# b = a + 2
# a = b * 4
# b = a / 3.14
# a = b - 8

# subtotal = 23
# total = subtotal * 0.15
# print(total)

# number = 1234567.456
# print(f'{number:,.1f}')

# name = input("Ваше имя: ")
# adress = input("Ваш адрес: ")
# phone_number = input("Ваш номер телефона: ")
# proffesion = input("Ваша специализация: ")

# print(name)
# print(adress)
# print(phone_number)
# print(proffesion)

# total_sales = float(input('Enter the project sales: '))
# profit = total_sales * 0.23
# print("The profit is", format(profit, ',.2f'))

# Input
# Divide
# Print

# acher = int(input("Enter the amount of achers: "))
# how_many = acher / 4047
# print(how_many)


# Узнаем цену для каждого
# good1 = float(input("Цена товара: "))
# good2 = float(input("Цена товара: "))
# good3 = float(input("Цена товара: "))
# good4 = float(input("Цена товара: "))
# good5 = float(input("Цена товара: "))

# TAX_RATE = 0.7

# subtotal = good1 + good2 + good3 + good4 + good5
# tax = subtotal * TAX_RATE
# total = subtotal + tax

# print("Итоговая сумма: ", format(total, ',.2f'))

# print ("Накопленная стоимость: ", format(subtotal, '.2f'))
# print ("Налог с продаж: ", format(tax, '.2f'))
# print ("Итоговая сумма: ", format(total, '.2f'))


# price = int(input('Price: '))
# TIPS = 0.18
# TAX = 0.7

# subtotal = price * TIPS * TAX
# total = price + subtotal

# print(format(total, ',.2f'))


# Упражнение по программированию 2.8

# Чаевые, налог и общая сумма

# Объявить переменные для стоимости еды, размера чаевых, налога и итоговой суммы.
food = 0.0
tip = 0.0
tax = 0.0
total = 0.0

# Константы для ставки налога и ставки чаевых.
TAX_RATE = 0.07
TIP_RATE = 0.18

# Получить стоимость еды.
food = float(input("Введите стоимость еды: "))

# Вычислить чаевые.
tip = food * TIP_RATE

# Вычислить налог.
tax = food * TAX_RATE

# Вычислить итоговую сумму.
total = food + tip + tax

# Напечатать чаевые, налог и итоговую сумму.
print("Чаевые: $", format(tip, '.2f'))
print("Налог: $", format(tax, '.2f'))
print("Итоговая сумма: $", format(total, '.2f'))


# End
