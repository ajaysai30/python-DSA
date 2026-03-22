import random

target = random.randint(0, 9)
guess = -1

while guess != target:
    guess = int(input("Guess number (0-9): "))

print("Correct!")
