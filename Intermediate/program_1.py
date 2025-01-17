#   1.Merge two lists into a single list.

list1 = [0,6,2,8,6]
list2 = [0,4,1,3,6]
print("List1:", list1)
print("List2:", list2)

mergedList = list1 + list2
print("MergedList:",mergedList)

#   2.Find the maximum and minimum values in a list.

sortedList = list(sorted(mergedList))
print("Sorted list:", sortedList)

max_value = sortedList[-1]
min_value = sortedList[0]

print("Maximum value:", max_value)
print("Minimum value:", min_value)

#   3.Remove duplicates from a list.

# Remove duplicates by converting to a set
uniqueList = list(set(mergedList))
print("Unique list:", uniqueList)

#   4.Iterate over a list and print each element.

for element in uniqueList:
    print(element)

#   5.Slice a list to get the first 5 elements.

slice_list = uniqueList[:5]
print("First 5 elements:",slice_list)

#   6.Create a list comprehension that squares each element in a given list.

squares_List = [element ** 2 for element in slice_list]
print("Squares List:", squares_List)

#   7.Check if a list is empty.

if len(uniqueList) == 0:
    print("Unique List is empty")
else:
    print("Unique List is not empty")

emptyList = []

if len(emptyList) == 0:
    print("Empty List is empty")
else:
    print("Empty List is not empty")

#   8.Create a new list that contains only the even numbers from an existing list.

even_numbers = [element for element in uniqueList if element % 2 == 0]
print("Even numbers:", even_numbers)

#   9.Remove all elements from a list.

squares_List.clear()
print("Squares List after clearing:", squares_List)

#   10.Replace all occurrences of a specific value in a list with another value.

replace_value = 8
new_value = 9

for element in range(len(mergedList)):
    if mergedList[element] == replace_value:
        mergedList[element] = new_value

print("Merged List after replacing:", mergedList)

