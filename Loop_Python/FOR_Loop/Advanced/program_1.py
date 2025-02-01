
#   1.	Write a loop to find the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    gcd = 1

    for i in range(1, min(a,b)+ 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return "The GCD of %d & %d is %d" % (a,b,gcd)

print(gcd(14,8))

#  2nd program are in program_2 file

#   3.	Use a loop to iterate through a nested dictionary and print all keys and values  	(e.g., { "info": { "name": "John", "age": 25 } }).

nested_dict = { "info": { "name": "John", "age": 25 } }

for key, value in nested_dict.items():
    for k, v in value.items():
        print(f"Key: {k}  Value: {v}")

#   4.	Write a loop to implement the bubble sort algorithm on a list of integers.

numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] < numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print("Sorted array is:", numbers)

#   5.	Use a loop to check if a string is an anagram of another string.

def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return "The words %s & %s are in anagram" % (str1,str2)
    else:
        return "The words %s & %s are not in anagram" % (str1,str2)

str1 = "listen"
str2 = "silent"
str3 = "listen"
str4 = "slent"

print(is_anagram(str1, str2))
print(is_anagram(str3, str4))

#   6.	Write a loop to flatten a 2D list into a 1D list (e.g., [[1, 2], [3, 4]] → [1, 2, 3, 4]).

nested_dict = [[1, 2], [3, 4]]

flattened_list = []

for sublist in nested_dict:
    for item in sublist:
        flattened_list.append(item)

print("Flattened list:", flattened_list)

#   7.	Use a loop to generate Pascal's triangle up to a given number of rows.

def pascal_triangle(n):
    for row in range(n):  # Outer loop for rows
        num = 1  # First value in each row is always 1
        print(" " * (n - row), end="")  # Center the triangle
        for col in range(row + 1):  # Inner loop for columns
            print(num, end=" ")  # Print the current value
            num = num * (row - col) // (col + 1)  # Compute next number in the row
        print()  # Move to the next line

pascal_triangle(5)

#   8.	Write a loop to calculate the power of a number without using the ** operator 	(e.g., 2^3 = 8).

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return '%d ^ %d = %d' %(base,exponent,result)

print(power(2, 3))

#   9.	Use a loop to filter and print only strings longer than 5 characters from a list.

strings = ["apple", "banana", "cherry", "date", "elderberry"]
length = 5

for word in strings:
    if len(word) > length:
        print(word)
    
#   10.	Write a loop to transpose a matrix (swap rows and columns in a 2D list).

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transposed_matrix = []

for j in range(len(matrix[0])):
    new_row = []
    for i in range(len(matrix)):
        new_row.append(matrix[i][j])
    transposed_matrix.append(new_row)

for row in transposed_matrix:
    print(row)

