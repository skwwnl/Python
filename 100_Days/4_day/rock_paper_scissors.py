import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

images = [rock, paper, scissors]

user = int(input("Go Human > "))
if user >= 3 or user < 0:
    print("Invalid, lose")
else:
    print(images[user])

    computer = random.randint(0, 2)
    print(f"Computer chose {images[computer]}")

    if user == 0 and computer == 2:
        print("User wins!")
    elif computer == 0 and user == 2:
        print("You lose")
    elif computer > user:
        print("You lose")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("Draw!")