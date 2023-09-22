# keep_going = 'y'

# while keep_going == 'y':
# 	sales = float(input('Enter sales: '))
# 	comm_r = float(input('enter comm rete: '))

# 	commision = sales * comm_r

# 	print(f"Commision is ${commision:,.2f}")

# 	keep_going = input('Do you want to calculate one more time? ')


# MAX_TEMP = 102.5

# temperature = float(input("Enter the substance's Celsius temperature: "))

# while temperature > MAX_TEMP:
# 	print('The temperature is too high.')
# 	print('Turn the thermostat down and wait')
# 	print('5 minutes. Then take the temperature')
# 	print('again and enter it.')
	
# 	temperature = float(input('Enter the new Celsius temperature: '))
# print('The temperature is acceptable.')
# print('Check it again in 15 minutes.')


# ## There are 2 types of Repetition structure or Loops
# ##  Condition-Controlled and Count-Controlled Loops

# for num in range(10, 5, -1):
# 	print(f'{num}')


# START = 60
# END = 131
# INCREMENT = 10
# VALUE = 0.6214

# print('KPH\tMPH')
# print('-------------------')

# for kph in range(START, END, INCREMENT):
# 	mph = kph * VALUE
# 	print(f'{kph}\t{mph:.1f}')



# for x in range(0, 6):
# 	print(x)

total = 0
for count in range(1, 6):
	total = total + count
	print(total)


