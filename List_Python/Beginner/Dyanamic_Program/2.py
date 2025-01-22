#   2.Access and print the first, middle, and last elements of a list.

myList = list(map(int, input().split()))
middleIndex = int((len(myList) - 1)/2)
print ("middleIndex:",middleIndex)
print ("First element:", myList[0])
print ("Middle element:", myList[middleIndex])
print ("Last element:", myList[-1])