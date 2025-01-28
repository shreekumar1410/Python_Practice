
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

#   6.	Write a loop to count the occurrences of a specific character in a string (e.g., count "a" in "banana").

words = "banana"
count = 0

for char in words:
    if char == 'a':
        count += 1

print(f"Count of 'a' in '{words}':", count)

#   7.	Use a loop to find the sum of all elements in an array [10, 20, 30, 40].

array = [10, 20, 30, 40]
sum = 0

for num in array:
    sum += num

print("Sum of elements in the array:", sum)

#   8.	Write a loop to check if a number is a palindrome (e.g., 121).

number = 121
copy_number = number
reversed_number = 0

for i in str(copy_number):
    reversed_number = reversed_number * 10 + int(copy_number % 10)
    copy_number //= 10
    
print("Reversed number:", reversed_number)

if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

