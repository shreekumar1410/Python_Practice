#   7.Reverse a list and print it.

myList = list(map(int, input().split()))

#Method 1:
# Create a new list that is a reversed list
rev = myList[::-1]

print(rev)

# Method 2:
# Initialize an empty list to store reversed element
res = []

# Loop through each item and insert
# it at the beginning of new list
for val in myList:
    res.insert(0, val)
print(res)