import random


print("random number guessing game")
print("guess a number from 1 to 10")

secret_number = random.randint(1, 10)
max_tries = 3

for attempt in range(1, max_tries + 1):
    guess_text = input(f"try {attempt}: ")

    if not guess_text.isdigit():
        print("please enter a whole number")
        continue

    guess = int(guess_text)

    if guess == secret_number:
        print("nice! you guessed it")
        break
    elif guess < secret_number:
        print("too low")
    else:
        print("too high")
else:
    print(f"out of tries. the number was {secret_number}")