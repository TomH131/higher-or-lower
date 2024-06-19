from random import randint

def random_number():
    """
    This function will  return a random number between 1 and 100
    """
    return randint(1, 100)

def guess_number():
    """
    This will allow the user to input a number in order to make
    their guess
    """
    return int(input("Please guess a number between 1 and 100:\n"))
    
def check_answer(guess, number):
    """
    This will check the user's guess against the random number and
    let the user know if they are correct or whether they need to 
    guess a higher or lower number
    """
    if guess == number():
        print("Congratulations! You guessed the correct number.")
        return True
    elif guess > number():
        print("Unlucky! Please guess a lower number.")
    else:
        print("Unlucky! Please guess a higher number.")
    return False

def start_game():
    """
    This function will start the game and also check for correct answer
    """
    number = random_number()
    correct = False
    while not correct:
        guess = guess_number()
        correct = check_answer(guess, number)

start_game()

