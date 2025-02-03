
#   1.	Write a loop to find the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    gcd = 1
    i = 1

    while i <= min(a,b)+1:
        if a % i == 0 and b % i == 0:
            gcd = i
        i += 1

    return "The GCD of %d & %d is %d" % (a,b,gcd)

print(gcd(14,3))

#  2nd program are in program_2 file

#   3.	Use a loop to iterate through a nested dictionary and print all keys and values  	(e.g., { "info": { "name": "John", "age": 25 } }).

nested_dict = { "info": { "name": "John", "age": 25 } }

def print_nested_dict_while(d):
    stack = [(d, 0)]

    while stack:
        current_dict, indent = stack.pop()
        
        for key, value in current_dict.items():
            if isinstance(value, dict):
                print("  " * indent + f"{key}:")
                stack.append((value, indent + 1))  
            else:
                print("  " * indent + f"{key}: {value}")

print_nested_dict_while(nested_dict)

#   4.	Write a loop to implement the bubble sort algorithm on a list of integers.

numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)
i = 0

while i < n:
    j = 0
    while j < (n-i-1):
        if numbers[j] > numbers[j+1] :
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        j += 1
    i += 1

print("Sorted array is:", numbers)