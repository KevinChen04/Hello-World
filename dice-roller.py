import random

rollAgain = True

sides = int(input("How many sides does your dice have?\n"))
rolls = int(input("How many dice do you want to roll?\n"))

while rollAgain:
    for i in range(rolls):
        number = random.randint(1, sides)
        print("Dice roll #" + str(i+1) + ": " + str(number))
        if number == sides:
            print(" *** Max roll! ***")

    user = str(input("Press q to exit or any key to roll again.\n"))
    if user.lower() == "q":
        rollAgain = False