
#   1. Write a loop to calculate the sum of all numbers from 1 to 100.

sum = 0
i = 0

while i <= 100:
    sum += i
    i += 1

print("Sum of 1 to 100:", sum)

#   2. Write a loop to reverse a given number (e.g., 12345 → 54321).

number = 12345
reversed_number = 0

while number > 0:
    reversed_number = (reversed_number * 10) + (number % 10)
    number //= 10

print("Reversed number:", reversed_number)

#   3. Use a loop to iterate through a dictionary { "a": 1, "b": 2, "c": 3 } and print keys and values.

dictionary = { "a": 1, "b": 2, "c": 3 }

keys = list(dictionary.keys())

index = 0

while index < len(keys):
    print(f"Key: {keys[index]}  Value: {dictionary[keys[index]]}")
    index += 1

#   4. Write a loop to print the multiplication table for a given number (e.g., 5). 

number = 5
i = 0

while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i += 1

#   5. Use a loop to find the first 10 numbers in the Fibonacci sequence.

fibonacci_sequence = [0, 1]

while len(fibonacci_sequence) < 10:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

print("Fibonacci sequence:", fibonacci_sequence)

#   6. Write a loop to count the occurrences of a specific character in a string (e.g., count "a" in "banana").

words = "banana"
eg_word = list(words)
finding_letter = 'a'
count = 0
len(eg_word)
i = 0

while i < len(eg_word):
    if eg_word[i] == finding_letter:
        count += 1
    i += 1

print(f"Count of character {finding_letter} in the {words}:", count)

#   7. Write a loop to find the sum of all elements in an array (e.g., [10, 20, 30, 40]).

array = [10, 20, 30, 40]
sum = 0
i = 0

while i < len(array):
    sum += array[i]
    i += 1

print("Sum of elements in the array:", sum)

#   8. Write a loop to check if a number is a palindrome (e.g., 121).

number = 1231
copy_number = number

while copy_number > 0:
    reversed_number = (reversed_number * 10) + (copy_number % 10)
    copy_number //= 10

if number == reversed_number:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")

#   9. Use a loop to print all prime numbers between 1 and 50.

i = 2
number = 50
prime_number = []

while i <= number+1:
    is_prime = True
    j = 2
    while j <= int(i**0.5):
        if i%j == 0:
            is_prime = False
            break
        j += 1

    if is_prime:
        prime_number.append(i)
    i += 1

print("Prime numbers between 1 and 50:", prime_number)

#   10.	Write a loop to iterate through a 2D list (matrix) and print each element.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0


while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        print(matrix[i][j], end=" ")
        j += 1
    print()
    i += 1






