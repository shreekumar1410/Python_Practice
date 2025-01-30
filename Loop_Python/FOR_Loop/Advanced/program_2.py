
#   2.	Write a loop to simulate a basic number guessing game with unlimited tries.

import random

secret_number = random.randint(1,10)

for i in range(100):
    guess_number = int(input("Enter the number(1-10) :"))
    if guess_number > secret_number:
        print ("Wrong number, expected less number.")
        continue
    elif guess_number < secret_number:
        print ("Wrong number, expected greater number.")
        continue
    else:
        print ("Congratulations! You guessed the number correctly.")
        break
    