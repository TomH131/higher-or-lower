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
            guess = int(input("Input your guess here:\n"))
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
        print("Please guess a lower number.")
    else: 
        print("Please guess a higher number.")
    
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
    This function will start the game
    """
    number = random_number()
    correct = False
    attempts = 0
    while not correct and attempts < 5:
        guess = guess_number()
        warm_cold(guess, number) 
        correct = check_answer(guess, number, attempts)
        attempts += 1

print("Welcome to a game of higher or lower. You will have 5 attempts to guess a random number between 1 and 100.")
start_game()

# Timer, Difficulty level (10, 50, 100)