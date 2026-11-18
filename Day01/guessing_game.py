import random

secret = random.randint(1, 100)
MAX_ATTEMPTS = 7
attempts = 0
won = False

while attempts < MAX_ATTEMPTS:
    guess = int(input("Enter a number between 1 and 100: "))
    attempts += 1

    if guess < secret:
        print("too low")
    elif guess > secret:
        print("too high")
    else:
        won = True
        break

if won:
    print("Correct!")
    print(f"Attempts: {attempts}")
else:
    print(f"Limit exceeded. The number was {secret}")