# def get_choices():
#     player_choice = "rock"
#     computer_choice = "paper"
#     return computer_choice
# def greeting():
#     return "Hi"
# response = greeting()
# print(response)
# choices = get_choices()
# print(choices)

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity: ")


# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("I love " + celebrity)


# Tuples(immutable sequences)

# coordinates = (4, 5)      # We can't modify data inside Tuples !!!
# coordinates =[1] = 10     # It doesnt work because tuples are immutable
# print(coordinates[1])


# Functions

# def say_hi(name, age):
#     print("Hello " + name + ", you are " + str(age))


# say_hi("Mike", "35")
# say_hi("Alex", "70")


# Return statement

# def cube(num):
#     return num*num*num
#     print("code")  # return breakes the function and after return print wont work

# result = cube(4)
# print(result)

# If statement

# is_male = False
# is_tall = True

# if is_male and is_tall:
#     print('you are a tall male')
# elif is_male and not (is_tall):
#     print("Yoa are a short male")
# elif not (is_male) and is_tall:
#     print("You are NOT a male but tall.")
# else:
#     print('you are either not male or not male or both')


# If Statements & Comparisons


# def max_num(num1, num2, num3):  # Programm for finding MAX number
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3


# print(max_num(323, 40, 5))  # MAX number will be printed

# # Building a Better Calculator

# num1 = float(input('Enter first number: '))
# op = input('Enter operator: ')
# num2 = float(input('Enter second number: '))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator.")


# Dictionoaries

# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
#     0: "Zero",       # * Numbers are also available
#     1: "One",
# }

# print(monthConversions.get("Luv", "Not a valid key"))
## при get если была недопустимое значение то
## посде запяятой можно ПЕРЕДАТЬ значение неправильносу значенид

# # ! There are two ways to get data from Dicrionary
# print(monthConversions.get("Dec"))  # Using .get("")
# print(monthConversions["Aug"])      # Using [""] mait method
# print(monthConversions[0])
# print(monthConversions.get(1))

# def hello_world(name):
#     print("Hello " + name)

# hello_world("Kirillos")



####@@@@ While Loop
# It allows us to look through and execute a block of code multiple times

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# print("Done with loop")

       ##@@@ Guessing game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False


# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True

# if out_of_guesses:
#     print("Out if guesses, You LOSE!")
# else:
#     print('You win!')




##$$$$ FOR loop
# friends = ['fafas', 'afasdf', 'fasdf']

# for index in range(5):
#     if index == 0:
#         print("first")
#     else:
#         print('second')


###$$$    Exponent Function            НЕ ПОНЯЛ!!!!!!

# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result

# print(raise_to_power(2, 3))


###@@@@  2D Lists & Nested loops

# number_grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]

# for row in number_grid:
#     for col in row:
#         print(col)



## ### @@@@ Try Except    to catch an error or invalif input

# try:
#     answer = 10 / 0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("Invalid error")



###### Reading files    @@@@@@@@@@@@

# asq = open("00.Modules_and_Pip.py", "w")
# asq.write("### Modules and Pip   @@@@@@@@@@@@")
# asq.close()


ex = open("testil.py", "w")
ex.write("Hello World")
ex.close()


