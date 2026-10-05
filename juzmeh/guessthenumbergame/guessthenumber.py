import random
secret_number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")
while True:
    guess = int(input("Enter your guess: "))
    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Correct! You guessed the number!")
        break