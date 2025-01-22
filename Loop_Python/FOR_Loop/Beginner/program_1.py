#   1.	Write a loop to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

#   2.	Write a loop to print "Hello, World!" 5 times.

for i in range(5):
    print("Hello, World!")

#   3.	Use a for loop to print the square of each number from 1 to 5.

for i in range(1, 6):
    print(i**2)

#   4.	Write a loop to calculate the sum of numbers from 1 to 10.

sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)

#   5.	Use a loop to iterate through an array [2, 4, 6, 8] and print each number.

arr = [2, 4, 6, 8]
for i in arr:
    print(i)

#   6.  Write a loop to iterate through the characters of the string "Python" and print each character.

str = "Python"
for char in str:
    print(char)

#   7.	Write a loop to find the factorial of a number (e.g., 5).

num = 5
factorial = 1
for i in range(1, num+1):
    factorial *= i
print("Factorial:", factorial)

#   8.  Use a loop to print all even numbers from 2 to 20.

for i in range(2, 21, 2):
    print(i)

#   9.	Write a loop to iterate through a list of fruits ["Apple", "Banana", "Cherry"] and print each fruit.

fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit)

#   10.	Write a loop to count down from 10 to 1.

for i in range(10, 0, -1):
    print(i)
