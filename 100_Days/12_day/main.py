import random


logo = """
 _______               ___.                 
 \      \  __ __  _____\_ |__   ___________ 
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
\____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/    \/     \/       
"""

number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
type_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if type_choice == "easy":
    attempts = 10
elif type_choice == "hard":
    attempts = 5
    
for i in range(attempts, 0, -1):
    print(f"You have {i} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.")
        if i == 1:
            print("You've run out of guesses, you lose.")
            break
        print("Guess again.")
    elif guess < number:
        print("Too low.")
        if i == 1:
            print("You've run out of guesses, you lose.")
            break
        print("Guess again.")
    else:
        print(f"You got it! The answer was {number}.")
        break