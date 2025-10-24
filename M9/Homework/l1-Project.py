import random

secret_number = random.randint(1, 100)
guess = 0

print("Guess the number between 1 and 100")

while guess != secret_number:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        if guess < secret_number:
            print("Too low Try again.")
        elif guess > secret_number:
            print("Too high Try again.")
        else:
            print("Congratulations You guessed it right!")
    else:
        print("Please enter a valid number.")