#   1.	Write a while loop to print numbers from 1 to 10.

i = 1
while i <= 10:
    print(i)
    i += 1

#   2.	Write a while loop to print "Hello, World!" 5 times.

i = 0
while i < 5:
    print("Hello, World!")
    i += 1

#   3.	Use a loop to print the square of each number from 1 to 5.   

i = 1
while i <= 5:
    square = i * i
    print(f"The square of {i} is {square}")
    i += 1

#   4.	Write a loop to calculate the sum of numbers from 1 to 10.

i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
    print(f"The sum of numbers from 1 to {i-1} is {sum}")

#   5.	Use a loop to iterate through an array [2, 4, 6, 8] and print each number.

array = [2, 4, 6, 8]
i = 0
while i < len(array):
    print(array[i])
    i += 1

#   6.  Write a loop to iterate through the characters of the string "Python" and print each character.

string = "Python"
i = 0
while i < len(string):
    print(string[i])
    i += 1

#   7.	Write a loop to find the factorial of a number (e.g., 5).

number = 5
factorial = 1
i = 1
while i <= number:
    factorial *= i
    i += 1
print(f"The factorial of {number} is {factorial}")

#   8.  Use a loop to print all even numbers from 2 to 20.

i = 2
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#   9.	Write a loop to iterate through a list of fruits ["Apple", "Banana", "Cherry"] and print each fruit.

fruits = ["Apple", "Banana", "Cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

#   10.	Write a loop to count down from 10 to 1.\

i = 10
while i >= 1:
    print(i)
    i -= 1
    
