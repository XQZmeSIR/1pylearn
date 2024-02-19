# CONCEPT: A loop that is inside another loop is called a nested loop.

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)
# # The output will be from 0:0:0 to 23:59:59  
#  # This program averages test scores. It asks the user for the
#  # number of students and the number of test scores per student.
# num_students = int(input('How many students do you have? '))
# num_test_scores = int(input('How many test scores per student? '))
# for student in range(num_students):
#     total = 0.0
#     print(f'Student number {student + 1}')
#     print('-----------------')
#     for test_num in range(num_test_scores):
#         print(f'Test number {test_num + 1}', end='')
#         score = float(input(': '))
#         total += score
#     average = total / num_test_scores
#     print(f'The average for student number {student + 1} '
#     f'is: {average:.1f}')
#     print()


# Printing Patterns
# rows = int(input('How many rows? '))
# cols = int(input('How many collomns? '))

# for row in range(rows):
#     for col in range(cols):
#         print('*', end='')
#     print()
# BAXE = 8

# for row in range(BAXE):
#     for col in range(row+1):
#         print('*', end='')
#     print()


# NUM_STEPS = 6
# for r in range(NUM_STEPS):
#     for c in range(r):
#         print(' ', end='')
#     print('#')