from random import randint


def random_number(difficulty):
    """
    This function will return a random number with a range
    dependent on the difficulty level chosen.
    """
    if difficulty == "easy":
        return randint(1, 25)
    elif difficulty == "medium":
        return randint(1, 100)
    elif difficulty == "hard":
        return randint(1, 200)
    elif difficulty == "extreme":
        return randint(1, 1000)


def check_difficulty():
    """
    This is to let the user choose the difficulty level and
    make sure one of three options has been chosen.
    """
    while True:
        difficulty = (
            input("Choose the difficulty level (easy, medium, hard or extreme): \n")
            .lower()
            .strip()
        )
        if difficulty in ["easy", "medium", "hard", "extreme"]:
            return difficulty
        else:
            print(
                "Sorry, please select one of the difficulty options: "
                "easy, medium, hard or extreme. \n"
            )


def guess_number(difficulty):
    """
    This will allow the user to input a number in order to make their guess
    """
    while True:
        try:
            guess = int(input("Input your guess here:\n"))
            if validate_guess(guess, difficulty):
                return guess
        except ValueError:
            print("That's not a number! Please enter a number.\n")


def validate_guess(guess, difficulty):
    """
    Checking the number guessed is valid.
    """
    ranges = {
        "easy": (1, 25),
        "medium": (1, 100),
        "hard": (1, 200),
        "extreme": (1, 1000)
        }

    low, high = ranges[difficulty]
    if not (low <= guess <= high):
        print(
            f"""You entered {guess}. Please enter a number
between {low} and {high}.\n"""
        )
        return False
    return True


def check_answer(guess, number, attempts):
    """
    This will check the user's guess against the random number and
    let the user know if they are correct or whether they need to
    guess a higher or lower number
    """
    if guess == number:
        print("Congratulations! You guessed the correct number.\n")
        return True
    if attempts == 4:
        print(
            f"""Unfortunately, you've now run out of attempts.
The number was {number}.\n"""
        )
        return False
    if guess > number:
        print("Please guess a lower number.\n")
    else:
        print("Please guess a higher number.\n")

    print(f"You have {4 - attempts} attempts left.")
    return False


def warm_cold(guess, number):
    """
    This will give the user some idea of how close they are to the answer
    """
    difference = abs(number - guess)

    if difference == 0:
        return
    elif difference <= 2:
        print("You're scorching!")
    elif difference <= 10:
        print("You're warm.")
    elif difference <= 25:
        print("You're cold.")
    else:
        print("You're freezing.")


def start_game():
    """
    This function will start the game, assign the number,
    start the attempts of at 0.
    """
    difficulty = check_difficulty()
    number = random_number(difficulty)
    correct = False
    attempts = 0

    """
    This will keep the game running until the correct answer
    is given or until the user has reached 5 attempts. Also
    provides feedback and increases the attempts by 1.
    """
    while not correct and attempts < 5:
        guess = guess_number(difficulty)
        warm_cold(guess, number)
        correct = check_answer(guess, number, attempts)
        attempts += 1

    new_game()


def new_game():
    """
    This function is to give the user the opportunity to play again
    """
    while True:
        response = (
            input("Would you like to play again? (yes/no)\n")
            .lower()
            .strip()
            )

        if response == "yes":
            start_game()
        elif response == "no":
            print("Thank you for playing.")
            return False
        else:
            print("Invalid input. Please enter 'yes or 'no'.")


print(
    """Welcome to a game of higher or lower.\n
You will have 5 attempts to guess a random number with
a range depending on the difficulty level you choose.\n
If you choose easy you will have to guess a number between 1 and 25.
Medium is a number between 1 and 100 and hard is a number between 1
and 200. Or you can attempt extreme and try to guess a number between
1 and 1000. Good luck!\n"""
)

start_game()
