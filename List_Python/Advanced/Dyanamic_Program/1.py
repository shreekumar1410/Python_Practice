list1 = list(map(int, input("Enter the frist list:").split()))

#   1.Find the second-largest number in a list.

sorted_list = sorted(list(list1))
second_largest_number = sorted_list[-2]
print("Second-largest number in the list:", second_largest_number)