list1 = list(map(int, input("Enter the frist list: ").split()))

#   1.Find the second-largest number in a list.

UniqueList = list(set(list1))
second_largest_number = UniqueList[-2]
print("Second-largest number in the list:", second_largest_number)

#   2.Split a list into two halves.

half1 = list1[:len(list1)//2]
half2 = list1[len(list1)//2:]
print("first half in the list:", half1)
print("second half in the list:", half2)

#   3.Rotate a list to the left by n positions.

n = int(input("Enter the number of positions: "))
rotated_list = list1[-n:] + list1[:-n] 
print(rotated_list)