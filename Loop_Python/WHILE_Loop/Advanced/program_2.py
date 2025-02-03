
#   2.	Write a loop to simulate a basic number guessing game with unlimited tries.

import random

no = 10
WA = 100
secret_number = random.randint(1,no)
i = 1

while i<WA:
    guess_number = int(input("Enter the number(1-10) :"))
    if guess_number > secret_number:
        print ("Wrong number, expected less number.")
    elif guess_number < secret_number:
        print ("Wrong number, expected greater number.")
    else:
        print (f"Congratulations! You guessed the number correctly in {i} Attempts. ")
        break
    
    if i % 5 == 0:
        choice = input("Do you want to reveal the number? (yes/no): ").strip().lower()
        if choice == "yes":
            print(f"The correct number was: {secret_number}")
            break 
        else:
            print("Keep guessing!")
    i += 1
    