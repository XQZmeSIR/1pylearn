print("Welcome to my computer quiz!")  # We're welcoming our user

# Asking him wether he wants to play or not
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

# Asking the first question using If statemant
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Asking the second question using If statemant
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Asking the third question using If statemant
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


# Asking the forth question using If statemant
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str((score/4) * 100) + "%.")  # We're showing User's score
print("Thank you for playing Quiz Game!")     # And we thank him\her
