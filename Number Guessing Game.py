import random

print("Welcome to the number guessing game")

while True:
    try:
        upper = int(input("Enter the maximum number: "))
        break
    except:
        print("Invalid input!")

number = random.randint(0, upper)
tries = 0

print("A random integer between 0 and", upper, "has been generated")

while True:
    try:
        guess = int(input("Guess the number: "))
        tries += 1
        break
    except:
        print("Invalid input!")

while guess != number:
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    while True:
        try:
            guess = int(input("Guess the number: "))
            tries += 1
            break
        except:
            print("Invalid input!")

print("You guessed the number correctly in", tries, "tries")