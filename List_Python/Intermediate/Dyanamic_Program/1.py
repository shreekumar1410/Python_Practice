#   1.Merge two lists into a single list.

list1 = list(map(int, input("Enter the Frist List:").split()))
list2 = list(map(int, input("Enter the Second List:").split()))

print("Frist List:", list1)
print("Second List:", list2) 

print("MergedList:",list1 + list2)
