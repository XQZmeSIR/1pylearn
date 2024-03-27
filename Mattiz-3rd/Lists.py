# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")

# numbers = list(range(1, 11))
# print(numbers)

# squares = []
# for value in range(1, 11):
#     squares.append(value ** 2)
#
# print(squares)  # this is code

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# one_million = [one for one in range(1, 1000001)]
# print((sum(one_million)))

# num = [one for one in range(1, 21, 2)]
# print(num)
#
# num = []
# for _ in range(3, 31, 3):
#     num.append(_)
#
# print(num)
#
# num = []
# for i in range(1, 11):
#     cube = i ** 3
#     num.append(cube)
# print(num)
#
# second method using list comprehension
# num = [cube**3 for cube in range(1, 11)]
# for cube in num:
#     print(cube)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[1:4])
# print(players[1:])
# print(players[:5])
# print(players[-4:])
# print('Let me introduce players:')
# for player in players[:3]:
#     print(player.title())

# my_food = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
# print("The first three items in the list are:", my_food[:4])
# print("The last three items are:", my_food[-3:])

# pizzas = ['peproni', 'margarita', 'meat', 'pineapple']
# pizzas2 = pizzas[:]
# pizzas.append('cheeze')
# pizzas2.append('ossetian')
# print("my pizzas:")
# for i in pizzas:
#     print(i)
# print("------------------")
# print("friend pizzas:\n")
# for j in pizzas2:
#     print(j)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# print("Let me present you a list of food:")
# for food in my_foods:
#     print(f'This is: {food}')

# what_i_did_today = ['woke up', 'went outside', 'journal', 'pla']
# def main():
#     print('27 March 2024')
#     print('-------------')
#     print(f'''First I {what_i_did_today[0]}
# then I {what_i_did_today[1]} to get some {exposure()}.
# ''')
#     print('I guess, according to decisive moments'
#           'I started day very well. I got', what_i_did_today[-1])
#     print("And finally, as you see, I'm doing PLA :)")
# def exposure():
#     what_i_did_today.append('sun exposure')
#     return what_i_did_today[4]
#
# if __name__ == '__main__':
#     main()

what_i_did_today = ['woke up', 'went outside', 'journal', 'pla']

last_activity = what_i_did_today.pop()  # revome and further access
print("Last what I did was:", last_activity) # to last item or by index

# Remember that each time you use pop(),
# the item you work with is no longer stored in the list.
# If you’re unsure whether to use the del statement
# or the pop() method, here’s a simple way to decide:
# when you want to delete an item from a list and not use that item
# in any way, use the del statement;
# if you want to use an item as you remove it, use pop() method.


#
