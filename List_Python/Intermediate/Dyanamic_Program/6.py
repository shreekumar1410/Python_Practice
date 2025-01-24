list1 = list(map(int, input("Enter the Frist List:").split()))

#   6.Create a list comprehension that squares each element in a given list.

uniqueList = list(set(list1))

squares_List = [element ** 2 for element in uniqueList]
print("Squares List:", squares_List)