import random

def number_guessing_game():
    random_number = random.randint(1, 100)
    
    max_attempts =7

    for attempt in range(1, max_attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess → "))
        if guess < random_number:
            print("Too low!\n")
        elif guess > random_number:
            print("Too high!\n")
        else:
            print(f"Congratulations! You guessed the number {random_number} in {attempt} attempts!")
            break
    else:
        print(f"Sorry, you’re out of attempts. The correct number was {random_number}.")


