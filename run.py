from random import randint

def random_number():
    return randint(1, 100)

def guess_number():
    return int(input("Please guess a number between 1 and 100:"))
    
def check_answer(guess, number):

    if guess == number():
        print("Congratulations! You guessed the correct number.")
        return True
    elif guess > number():
        print("Unlucky! Please guess a lower number.")
    else:
        print("Unlucky! Please guess a higher number.")
    return False

def start_game():
    number = random_number()
    correct = False
    while not correct:
        guess = guess_number()
        correct = check_answer(guess, number)

start_game()

