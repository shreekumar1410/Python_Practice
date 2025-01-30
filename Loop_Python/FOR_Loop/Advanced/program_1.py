
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


