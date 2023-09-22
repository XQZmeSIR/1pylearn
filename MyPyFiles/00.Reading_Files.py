### Reading files in Python is done by open()
##  "r" to read a file
##  "w" to write/change a file
##  "a" to append new info to file
##  "r+" to read and write a file
## .close()  to close file
# employee_file = open("employees.txt", "r")

# ##        how to check if the file is readable
# # print(employee_file.readable())     # This is gonna retrn boolean value 
# #print(employee_file.read())      ## read

# for employee in employee_file.readlines():
# 	print(employee)

# # print(employee_file.readlines()[1])      ##this read file and puts them in list



# employee_file.close()


### Write to files @@@@@@@@@@@@@@@@@

employee_file = open("index.html", "w")

employee_file.write('<p>This is HTML</p>')

employee_file.close()


### Lets say i want to create a new file for my
### Python learning. I can do it mannualy or ...
hell = open("testHTML.html", "w")
hell.write("<p>See? Isn't it cool!</p>")
hell.close()

