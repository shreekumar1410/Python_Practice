#   9.Find the index of a specific element in a list.

myList = list(map(int, input().split()))
element = int(input("Enter the element you want to search:"))

for i in range(len(myList)):
    for j in range(0, len(myList) - i - 1):
        if myList[j] > myList[j + 1]:  # Swap if the current element is greater than the next
            myList[j], myList[j + 1] = myList[j + 1], myList[j]

print( myList)

specific_element_index=myList.index(element)

print ("Index of element", element, ":", specific_element_index)

#   10. Count the occurrences of a specific value in a list.

element = int(input("Enter the element you want to count:"))
count = myList.count(element)

print ("Count of element", element, ":", count)