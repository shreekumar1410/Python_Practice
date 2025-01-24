#   2.Find the maximum and minimum values in a list.

list1 = list(map(int, input("Enter the Frist List:").split()))

sortedList = list(sorted(list1))

max_value = sortedList[-1]
min_value = sortedList[0]

print("Maximum value:", max_value)
print("Minimum value:", min_value)

#   3.Remove duplicates from a list.

uniqueList = list(set(sortedList))

print("Unique list:", uniqueList)

#   4.Iterate over a list and print each element.

for element in uniqueList:
    print(element)

#   5.Slice a list to get the first 5 elements.

length = len(uniqueList)

n = int(input(f"Enter the value for slice (within {length}): "))

slice_list = uniqueList[:n]
print(f"First {n} elements:",slice_list)

