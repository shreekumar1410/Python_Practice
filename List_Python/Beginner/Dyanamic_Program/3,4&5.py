#   3.Append an element to a list and print the updated list.

myList = list(map(int, input().split()))

myList.append(12)
print ("Updated list(After appended):", myList)

#   4.Remove the third element from a list.

myList.pop(2) #Remove the third element from a list
print ("Updated list(After removed):", myList)

#   5.Find the length of a given list.

length = int((len(myList)))
print ("Length of the list:", length)
