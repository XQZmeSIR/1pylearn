# Функци с возвратом и модули

# import random

# def main():
#     for i in range(5):
#         print(f'Number is: {random.randint(1, 1000):^5d}')


# main()


# ######### dice and using the random numbers ############

# До тех пор, пока пользователь хочет бросить кубики:
# Показать случайное число в диапазоне от 1 до 6
# Показать еще одно случайное число в диапазоне от 1 до 6
# Спросить пользователя, хочет ли он бросить кубики еще раз

# import random
# MIN = 1
# MAX = 6

# def main():
#     n = 'n'
#     y = 'y'
#     while True:
#         input('Do u want to dice a roll? (y=yes) (n=no): ')
#         if y == 'y':
#             print('Rolling the dices...')
#             print(f'The first roll is: {random.randint(MIN, MAX)}')
#             print(f'The second roll is: {random.randint(MIN, MAX)}')
#         else:
#             break
  
# main()
# Мои Ошибки
# # 1. Надо было создать переменную для инпута и ее использовать для if цикла
# # 2. Использовать elif для НЕТ
# # 
# #######################  
# import random

# MIN = 1
# MAX = 6

# def main():
#     while True:
#         choice = input('Do you want to roll the dice? (y=yes, n=no): ')
#         if choice == 'y':
#             print()
#             print('Rolling the dice...')
#             print()
#             print(f'The first roll is: {random.randint(MIN, MAX)}')
#             print(f'The second roll is: {random.randint(MIN, MAX)}')
#             print()
#         elif choice == 'n':
#             break
#         else:
#             print('Invalid choice. Please enter "y" or "n".')

# main()



# It is a Diceware programm for creating passphrases
# using ordinary dice as a random number generator.

# import random

# MIN = 1
# MAX = 6

# def main():
#     while True:
#         choice = input('Do you want to roll the dice? (y=yes, n=no): ')
        
#         if choice == 'y':
#             def roll_dice():
#                 print()
#                 print('Rolling the dice...')
#                 print()
#                 print(f'The first roll is: {random.randint(MIN, MAX)}')
#                 print(f'The second roll is: {random.randint(MIN, MAX)}')
#                 print(f'The third roll is: {random.randint(MIN, MAX)}')
#                 print(f'The fourth roll is: {random.randint(MIN, MAX)}')
#                 print(f'The fifth roll is: {random.randint(MIN, MAX)}')
#                 print()
#                 print('The dice were rolled')
#         elif choice == 'n': # n in case I don't want to continue.
#             break
#         else:               # Sentinel(if its called like that.)
#             print('Invalid choice. Please enter "y" or "n".')


# main()

# import random

# MIN = 1
# MAX = 6

# def main():
#     while True:
#         choice = input("Do you want to roll the dice? (y=yes) (n=no) ")
#         if choice == 'y':
#             roll_dice()
#         elif choice == 'n':
#             break

# def roll_dice():
#     for i in range(5):
#         print(f'The roll is: {random.randint(MIN, MAX)}')


# main()

# import random

# HEADS = 1
# TAILS = 2
# TOSSES = 10

# def main():
#     for toss in range(TOSSES):
#         if random.randint(HEADS, TAILS) == HEADS:
#             print('Орел')
#         else:
#             print('Решка')


# main()



# import random
# number1 = random.randrange(0, 101, 10)
# number2 = random.random()
# number3 = random.uniform(1.0, 10.0)
# print(number1)
# print(number2)
# print(number3)





# ############### Functions with RETURN  ##################################

# def main():
# 	first_age = int(input('Age: '))

# 	second_age = int(input('Age fritnd: '))

# 	total = sum(first_age, second_age)

# 	print(f'U are {total} age.')
	

# def sum(num1, num2):
# 	return num1 + num2


# main()


# wrote by myself
# def main():
# 	print("We'd like to know your position in this company.")
# 	years = int(input("Enter the number of years: "))

# 	output = get_an_age(years)
# 	print(f'Youll need {output} years in sum to get a promotion')

# def get_an_age(number):
# 	return number + 2

# main()

def get_regular_price():
	price = float(input("Введите обычную цену товара: "))
	return price

get_price = get_regular_price()
print(int(get_price))


