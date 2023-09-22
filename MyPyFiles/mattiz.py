# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great and cunning trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# for value in range(6):
#     print(value)

# squares = []
# for value in range(1,11):
    # square = value**2
    # squares.append(square)
# print(squares)

# digits = [0,1,2,3,4,5,6,7,8,9,0]
# min()
# squares = [value**2 for value in range(1,11)]  # Генератор списков !!!!!!!
# print(squares)


# for number in range(1, 11, 2):
#     print(number)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:])
# print(players[:4])
# print(players[-3:])
# prinVt(players[0:5:2])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:

# my_food = ['pizza', 'falafel', 'carrot cake']
# friend_food = my_food[:]

# my_food.append('tomato')
# friend_food.append('lavash')

# print("My favorite food is:")
# print(my_food)

# print("\nMy friend's favorite food is:")
# print(friend_food)

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())


# Чтобы узнать, присутствует ли заданное значение в списке,
# воспользуйтесь ключевым словом in.
## >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
## >>> 'mushrooms' in requested_toppings
## True
## >>> 'pepperoni' in requested_toppings
## False

# banned = ['andrew', 'maria', 'max']
# users = "alex" 

# if users not in banned:
#     print(f'{users.title()} you are allowed to post here!')

# print('Hello world!')



# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("\nFinished making your pizza!")

# available_toppings = ['mushrooms', 'olives', 'green peppers', 
#                        'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}.')
#     else:
#         print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making pizza!")


# list = {'color': 'green', 'height': 202, 'position': 'outside hitter'}
# list['height'] = 198
# print(list['color'])
# print(list['position'])
# print(list['height'])

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] = x_increment

# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alana = {
#         'profesion': 'volleyball player',
#         'gender': 'female',
#         'age': 25,
#         'position': 'opposite hitter',
#         'qualities': 'gorgeous, smart and talanted',
#         }
# print("Here's some info about Alana:")
# print(alana['profesion'].title())
# print(alana['gender'].title())
# print(alana['age'])
# print(alana['position'].title())
# print(alana['qualities'].title())


# user_0 = {
#         'username': 'efermi',
#         'first': 'enrico',
#         'last': 'fermi',
#         }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']             # Names that we need
# for name in favorite_languages.keys():  # Перебор списка using keys!!!!!!!!!
#     print(name.title())
#     if name in friends:                 # Проверяем совпадения
#             language = favorite_languages[name].title()
#             print(f"\t{name.title()}, I see you love {language}!")

# if 'erti' not in favorite_languages.keys():
#     print("Erin pdfjboabdf")

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank u for gweiogn/")


# print("The following languages have been mentioned:")
# for language in favorite_languages.values():  # Используем метод .values()
#     print(language.title())                   # для получ списка без ключей


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):     # Чтобы получить
# список выбранных языков без повторений, можно воспользоваться множеством
# (set)
# languages = {'python', 'ruby', 'python', 'c'}  Thats how mnojestva looks like
# It doesnt have keys and values in him.
    print(language.title())











