import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 51 and 100.")

number = random.randint(51, 100)
attempts = 5

while attempts > 0:
    guess = int(input("Take a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number} in {5 - attempts} attempts.")
        break       
    elif guess < number:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1

if attempts == 0:   
    print(f"You ran out of attempts. The answer was {number}.")

print("  Thanks for playing!")
