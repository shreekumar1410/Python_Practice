#   8.Sort a list of integers in ascending order.

myList = list(map(int, input().split()))

for i in range(len(myList)):
    for j in range(0, len(myList) - i - 1):
        if myList[j] > myList[j + 1]:  # Swap if the current element is greater than the next
            myList[j], myList[j + 1] = myList[j + 1], myList[j]

print("sorted list (ascending):", myList)

for i in range(len(myList)):
    for j in range(0, len(myList) - i - 1):
        if myList[j] < myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]

print("sorted list (descending):", myList)



