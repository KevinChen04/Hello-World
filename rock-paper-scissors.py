# Rock, Paper, Scissors game I pulled from
# https://github.com/Mrinank-Bhowmick/python-beginner-projects

while True:
    playerchoice, compchoice, value = (
        input("[R]ock, [P]aper, [S]cissors\n: ").lower(),
        __import__("random").randint(1, 3),
        0,
    )
    if playerchoice in ["r", "p", "s"]:
        break
    print("Not r, p, or s\n")

value = ["r", "p", "s"].index(playerchoice) + 1

if str(value) + str(compchoice) in ["13", "21", "32"]:
    print("You win!")
elif str(value) == str(compchoice):
    print("It's a draw!")
else:
    print("You lose.")
