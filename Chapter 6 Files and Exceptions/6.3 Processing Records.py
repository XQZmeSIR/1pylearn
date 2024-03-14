def main():
    num_emps = int(input("How many records do you want to create? "))

    with open('employees.txt', 'w') as emp_file:
        for count in range(1, num_emps + 1):
            print(f'Enter data about employee #{count}')
            name = input('Name: ')
            id_num = (input('ID: '))
            dept = input('Department: ')

            