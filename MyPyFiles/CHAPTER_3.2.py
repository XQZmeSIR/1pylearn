#  Игра в подсчитывание монет.

# print("Welcome to the game!")

# moneta1 = int(input('Enter the amount of 5 monet: '))
# moneta2 = int(input('Enter the amount of 10 monet: '))
# moneta3 = int(input('Enter the amount of 50 monet: '))

# total = moneta3 * 0.5 + moneta2 * 0.1 + moneta1 * 0.05

# if total == 1:
#     print('Congratulations! You won!')
# else:
#     if total < 1:
#         print('You collect less than you need.')
#     elif total > 1:
#         print('You collect more than you need.')
# print('Try one more time.')


# for your_speed_in_mph in range(60, 131, 10):
#     mph = your_speed_in_mph * CONST
#     print(
#         f'Youre speed in KPH {your_speed_in_mph} | Youre speed in MPH is {mph:,.1f}')


# This program converts the speeds 60 kph
# through 130 kph (in 10 kph increments)
# to mph.
# START_SPEED = 60
# # Starting speed
# END_SPEED = 131
# # Ending speed
# INCREMENT = 10
# # Speed increment
# CONVERSION_FACTOR = 0.6214
# # Conversion factor
# # Print the table headings.
# print('KPH\tMPH')
# print('--------------')
# # Print the speeds.
# for kph in range(START_SPEED, END_SPEED, INCREMENT):
#     mph = kph * CONVERSION_FACTOR
#     print(f'{kph}\t{mph:.1f}')


# for num in range(5, 0, -1):
    # print(num)

# MAX = 5
# total = 0.0

# print('Эта программа вычисляет сумму из')
# print(f'{MAX} чисел, которые вы введете.')

# for counter in range(MAX):
#     number = int(input('Enter the number: '))
#     total = total + number

# print(f'Cумма составляет {total}.')

# print("Hey User! What book do you want to read?")

# books = ['mattiz', 'gaddis', 'lutz']

# your_choice = input()

# if your_choice == books[0]:
#     print("Good choice!")
# your_choice == books[1]:
#     print("Bad choice")
# elif your_choice == books[2]:
#     print("Damn, that's a tought one. Good luck!")
# else:
#     print('Idiot, write it corrertly!')


# print ("Hey User! What book do you want to read?")

# books = ['mattiz', 'gaddis', 'lutz']

# your_choice = input()

# if your_choice == books[0]:
#     print ("Good choice!")
# else:
#     if your_choice == books [1]:
#         print ("Bad choice")
#     else:
#         if your_choice == books [2]:
#             print ("That's a tough one. Good luck!")
#         else:
#             print ("Write it correctly")


## Items works with pairs key-value
## Keys works with keys

# user_0 = {
#         'username': 'efermi',
#         'first': 'enrico',
#         'last': 'fermi',
#         }
# for k, v in user_0.items():
#     print(f"\nKey: {k}")
#     print(f"Value: {v}")


# set это множество

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# rivers = {
#     'volga': 'russia',
#     'nile': 'egypt',
#     'nikkatagua': 'africa',
#     'terek': 'russia'
# }

# for name in rivers.values():
#     print(f"{name}")


# for name, country in rivers.items():
#     print(f"The {name} runs through {country}.")


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)

# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[0:5]:
#     print(alien)



# Список в Словаре

## Save info about pizza
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }

# print(f"You order a {pizza['crust']}-crust pizza "
#     "with the following toppings:")

# for topping in pizza['toppings']:
#     print("\t" + topping)


### or - 1 is true
### and - both are true

# is_male = False
# is_tall = store_false

# if is_male or is_tall:
#     print('You are a tall male')

# else:
#     print()








#