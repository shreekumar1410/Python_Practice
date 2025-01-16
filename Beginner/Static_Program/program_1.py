#   1.Create a list of 10 numbers and print it.

myList= [4,8,7,1,1,7,10,5,4,1]
print("1.Create a list of 10 numbers and print it.")
print ("Orginal list:",myList)

#   2.Access and print the first, middle, and last elements of a list.

middleIndex = int((len(myList) - 1)/2)
print("2.Access and print the first, middle, and last elements of a list.")
print ("middleIndex:",middleIndex)
print ("First element:", myList[0])
print ("Middle element:", myList[middleIndex])
print ("Last element:", myList[-1])

#   3.Append an element to a list and print the updated list.

myList.append(12)
print("3.Append an element to a list and print the updated list.")
print ("Updated list(After appended):", myList)

#   4.Remove the third element from a list.

myList.pop(2) #Remove the third element from a list
print("4.Remove the third element from a list.")
print ("Updated list(After removed):", myList)

#   5.Find the length of a given list.

length = int((len(myList)))
print("5.Find the length of a given list")
print ("Length of the list:", length)

#   6.Check if a given element exists in a list.

element = 7
print("6.Check if a given element exists in a list.")
if element in myList:
    print ("Element", element, "exists in the list")
else:
    print ("Element", element, "does not exist in the list")

element=11
if element in myList:
    print ("Element", element, "exists in the list")
else:
    print ("Element", element, "does not exist in the list")

#   7.Reverse a list and print it.

revList = list(reversed(myList))
print("7.Reverse a list and print it.")
print ("Reversed list:", revList)

#   8.Sort a list of integers in ascending order.

sortedList = list(sorted(myList))
print("8.Sort a list of integers in ascending order.")
print ("Sorted list:", sortedList)

#   9.Find the index of a specific element in a list.

element = 7
specific_element_index=sortedList.index(element)
print("9.Find the index of a specific element in a list.")
print ("Index of element", element, ":", specific_element_index)

#   10.Count the occurrences of a specific value in a list.

element = 1
count = sortedList.count(element)
print("10.Count the occurrences of a specific value in a list.")
print ("Count of element", element, ":", count)