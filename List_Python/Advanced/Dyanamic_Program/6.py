list1 = list(map(int, input("Enter the Frist list:").split()))
list2 = list(map(int, input("Enter the Second list:").split()))

#   6.Find the common elements between two lists.

common_elements = [element for element in list1 if element in list2]
print("Common elements between the two lists:", common_elements)