# age = int(input("What's your age: "))

# if age <= 13:
#     print("You are a child")
# elif age >= 14 and age <= 24:
#     print("You are an aduld")
# elif age >= 24 and age <= 59:
#     print("You are a formed man")
# else:
#     print("You are an elderly")


# year = int(input())
# # Проверяем, выполняются ли условия для високосного года:
# # Год делится на 4 без остатка,
# # Год не делится на 100 без остатка, за исключением случаев, когда год делится на 400 без остатка.
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')


# r1 = int(input())
# r2 = int(input())
# c1 = int(input())
# c2 = int(input())

# if r1 == r2 or c1 == c2:
#     print("YES")
# else:
#     print("NO")


# # Получаем четыре координаты и сохраняем их в переменных x1, y1, x2, y2
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# # Вычисляем разность координат по осям x и y для определения хода короля
# x = x2 - x1  # разность координат по оси x
# y = y2 - y1  # разность координат по оси y
# # так как король может ходить во все направления, но только на одну клетку.
# if -1 <= x <= 1 and -1 <= y <= 1:
#     print('YES')
# else:
#     print('NO')


# x = int(input())
# y = int(input())

# print(f"Точка(x = {x}, y = {y})")

# print(f"{x = :.3f}")

# marks=[1,5,4,5,6]
# print(marks[4])
# a=[]
# a.append(34)
# print(a)
# print(len(marks))

# mass = int(input())  

# if mass <= 59:
#     print('Легкий вес')
# elif mass<= 63:
#     print('Первый полусредний вес')
# elif mass <=68
#     print('Полусредний вес')

# a = float(input())
# b = float(input())
# s = (a * b) / 2
# print(s)

# 6.1
# s = float(input())
# v1 = float(input())
# v2 = float(input())

# v = v1 + v2
# print(s/v)

# a = float(input())
# if a == 0:
#     print("Обратного числа не существует")
# else:
#     print(1 / a)

# grad = float(input())
# c = (5/9)*(grad - 32)
# print(c)

# n = int(input())
# if n <= 2:
#     print(n * 10.5)
# else:
#     print(21 + (n - 2) * 4)

# a = float(input())
# b = a * 10
# c = b % 10
# print(c)

# a = float(input())  # получаем число с плавающей запятой
# # из числа 'a' вычитаем число 'a' переведеное в целое(оставляя только дробную часть),
# # и выводит результат (дробную часть числа) на экран.
# print(a - int(a))

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())

# print('Наименьшее число =', min(a, b, c, d, e))
# # Выводим на экран строку с сообщением о наибольшем числе, 
# # найденном среди введенных значений, используя функцию max().
# print('Наибольшее число =', max (a, b, c, d, e))

# x = int(input())  # получаем целое число

# a = x % 10
# b = x // 10 % 10
# c = x // 100

# if a + b + c == 2 * max(a, b, c):
#     print("Число интересное")  # Выводим сообщение, если условие выполняется
# else:
#     print("Число неинтересное")  # Выводим сообщение, если условие не выполняется

# a = float(input())
# b = float(input())
# c = float(input())
# d = float(input())
# e = float(input())

# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# Получаем 4 целых числа и сохраняем в переменную'
# p1 = int(input())
# p2 = int(input())
# q1 = int(input())
# q2 = int(input())
#
# print(abs(p1 - q1) + abs(p2 - q2))

# name = input("")
# # surname = input("")
# print(f'Футбольная команда {name} имеет длину {len(name)} символов')

# a = input()  # получаем первый город
# b = input()  # получаем второй город
# c = input()  # получаем третий город

# a = input('')
# if 'синий' in a:
#     print('YES')
# else:
#     print('NO')
#
# mail = input(' ')
# if '@' not in mail and '.' not in mail:
#     print("NO")
# else:
#     print('YES')

# import math

# x1 = float(input())
# y1 = float(input())
# x2 = float(input())
# y2 = float(input())

# result = math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)

# print(math.sqrt(result))

# import math

# a=float(input())
# b=float(input())

# print((a+b) / 2)
# print(math.sqrt(a*b))
# print((2*(a*b)) / (a+b))
# print(math.sqrt(math.pow(a, 2) + math.pow(b, 2) / 2))

# import math

# n = int(input())
# a = float(input())

# s = (n * a**2) / (4 * math.tan(math.pi / n))
# print(s)

# for i in range(6):
#     print("AAA")
# for a in range(5):
#     print("BBBB")
# print("E")
# for c in range(9):
#     print("TTTTT")
# print("G")

# num = int(input())
# for i in range(num + 1):
#     print(f"Квадрат числа {i} равен {i**2}")

m = int(input())    # стартовое количество организмов
p = int(input())    # среднесуточное увеличение в %;
n = int(input())    # количество дней для размножения

for i in range(n):
    qw = m * (p / 100 + 1) ** i
    print(i + 1, qw)











#
