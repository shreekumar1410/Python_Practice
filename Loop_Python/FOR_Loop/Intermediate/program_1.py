
#   1.	Write a loop to calculate the sum of all numbers from 1 to 100.

sum = 0
for i in range(100):
    sum += i

print("Sum of 100 :", sum)

#   2.	Write a loop to reverse a given number (e.g., 12345 → 54321).

number = 12345
reversed_number = 0

for _ in str(number):
    reversed_number = reversed_number * 10 + int(number % 10)
    number //= 10

print("Reversed number :", reversed_number)

#   3.	Use a loop to iterate through a dictionary { "a": 1, "b": 2, "c": 3 } and print keys and values.

dictionary = { "a": 1, "b": 2, "c": 3 }

for key, value in dictionary.items():
    print(f"Key: {key}  Value: {value}")

#   4.	Write a loop to print the multiplication table for a given number (e.g., 5).

number = 5

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")

#   5.	Use a loop to find the first 10 numbers in the Fibonacci sequence.

fibonacci_sequence = [0,1]

for _ in range(8):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

print("Fibonacci sequence:" ,fibonacci_sequence)



