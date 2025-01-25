# list1 = list(map(int, input("Enter the frist list: ").split()))

# #   7.Write a program to check if a list is sorted.

# def is_sorted(a):
#       for i in range(len(a) - 1):

#         if a[i] > a[i + 1]:
#             return ("The Given List is Not Sorted")
#         elif all(a[i] >= a[i+1]):
#             return ("The Given List is Descending Sorted")
#         return ("The Given List is Ascending Sorted")


# print(is_sorted(list1))

list1 = list(map(int, input("Enter the first list: ").split()))

# Function to check if a list is sorted
def is_sorted(a):
    ascending = True
    descending = True

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:  # If any element is greater than the next, it's not ascending
            ascending = False
        if a[i] < a[i + 1]:  # If any element is smaller than the next, it's not descending
            descending = False

    if ascending:
        return "The Given List is Ascending Sorted"
    elif descending:
        return "The Given List is Descending Sorted"
    else:
        return "The Given List is Not Sorted"

# Print the result
print(is_sorted(list1))
