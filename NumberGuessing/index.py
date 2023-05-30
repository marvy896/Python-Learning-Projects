from random import randint


def playerRound():
    print("A number has been selected, from 1 to 100.")
    selectedNumb = randint(0, 100)
    while True:
        if numbGuess(selectedNumb):
            break

    print("Would you like to play again? Y/N")
    guessAgain = str(input("> "))
    if guessAgain == "Y":
        return False
    else:
        return True


def numbGuess(selectedNumb):
    guess = int(input("Enter a number: "))
    if guess < selectedNumb:
        print("Too low! Try again:")
        return False
    elif guess > selectedNumb:
        print("Too high! Try again:")
        return False
    else:
        print("Well done, that’s correct!")
        return True


print("Welcome to Number Guessing!")
while True:
    if playerRound():
        break
print("GoodBye")
