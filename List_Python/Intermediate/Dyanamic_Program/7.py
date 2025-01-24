list1 = list(map(int, input("Enter the Frist List:").split()))

emptyList = []

#   7.Check if a list is empty.

def check_list(a):
    if len(a) == 0:
        return ("The List is empty")
    else:
        return ("The List is not empty")

print(check_list(list1))

print(check_list(emptyList))