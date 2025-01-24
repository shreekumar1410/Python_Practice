list1 = list(map(int, input("Enter the Frist List:").split()))

#   9.Remove all elements from a list.

uniqueList = list(set(list1))

list1.clear()

print("Unique List:", uniqueList)

print("List after clearing:", list1)