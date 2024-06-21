from random import randint

def random_number():
    """
    This function will return a random number between 1 and 100
    """
    return randint(1, 100)

def guess_number():
    """
    This will allow the user to input a number in order to make
    their guess
    """
    while True:
        try:
            guess = int(input("Please input your guess here:\n"))
            if validate_guess(guess):
                return guess
        except ValueError:
            print("That's not a valid number! Please enter a number between 1 and 100.\n")

def validate_guess(guess):
    """
    Checking the number guessed is valid.
    """
    if guess < 1 or guess > 100:
        print(f"You entered {guess}. Please enter a number between 1 and 100.")
        return False
    return True

def check_answer(guess, number, attempts):
    """
    This will check the user's guess against the random number and
    let the user know if they are correct or whether they need to 
    guess a higher or lower number
    """
    if guess == number:
        print("Congratulations! You guessed the correct number.")
        return True
    if attempts == 4:
        print(f"Unfortunately, you've now run out of attempts. The number was {number}.")
        return False
    if guess > number:
        print("Unlucky! Please guess a lower number.")
    else: 
        print("Unlucky! Please guess a higher number.")
    
    return False

def start_game():
    """
    This function will start the game
    """
    number = random_number()
    correct = False
    attempts = 0
    while not correct and attempts < 5:
        guess = guess_number()
        correct = check_answer(guess, number, attempts)
        attempts += 1

print("Welcome to a game of higher or lower. You will have 5 attempts to guess a random number between 1 and 100.")
start_game()

# Timer, Difficulty level (10, 50, 100), warm/cold