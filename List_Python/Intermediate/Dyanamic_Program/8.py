list1 = list(map(int, input("Enter the Frist List:").split()))

#   8.Create a new list that contains only the even numbers from an existing list.

uniqueList = list(set(list1))

even_numbers = [element for element in uniqueList if element % 2 == 0]
print("Even numbers:", even_numbers)