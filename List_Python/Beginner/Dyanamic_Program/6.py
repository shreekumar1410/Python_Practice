#   6.Check if a given element exists in a list.

myList = list(map(int, input().split()))

element = int(input("Enter the element you want to find: "))

if element in myList:
    print ("Element", element, "exists in the list")
else:
    print ("Element", element, "does not exist in the list")