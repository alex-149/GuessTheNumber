import random

random_number = random.randint(1, 1000)

guesses_remaining = 5

for i in range(1, guesses_remaining + 1):
               
    x = int(input("Guess the number: "))
        
    if x == random_number:
        print("Correct")
        break

    if x != random_number:
            print("False")
            if x > random_number:
                print("Lower")
            if x < random_number:
                print("Higher")

    guesses_remaining = guesses_remaining - 1

if guesses_remaining == 0:
    print(f"You took to many attempts the number was {random_number}")