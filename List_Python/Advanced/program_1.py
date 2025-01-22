import random

list1 = [4,3,4,5,9]
list2 = [7,2,4,1,3]

#   1.Find the second-largest number in a list.

sorted_list = sorted(list(list1))
second_largest_number = sorted_list[-2]
print("Second-largest number in the list:", second_largest_number)

#   2.Split a list into two halves.

half1 = list1[:len(list1)//2]
half2 = list1[len(list1)//2:]
print("first half in the list:", half1)
print("second half in the list:", half2)

#   3.Rotate a list to the left by n positions.

n = 2
rotated_list = list1[-n:] + list1[:-n] 
print(rotated_list)

#   4.Flatten a nested list.

nested_list = [[1,2,4],[4,7,6],[9,8,2]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)

#   5.Create a matrix using lists and access specific rows and columns.

matrix = [[7,5,9],[4,3,9],[8,4,6]]

row1 = matrix[0]
column1 = [row[0] for row in matrix]

print("First row:", row1)
print("First column:", column1)
element = matrix[2][1]  
print("Element at (2, 1):", element)

#   6.Find the common elements between two lists.

common_elements = [element for element in list1 if element in list2]
print("Common elements between the two lists:", common_elements)

#   7.Write a program to check if a list is sorted.

def is_sorted(a):
      for i in range(len(a) - 1):

        if a[i] > a[i + 1]:
            return False
        return True

print(is_sorted(list1))

print(is_sorted(sorted_list))

#   9.Implement a function to shuffle a list randomly.

def myfunction():
  return 0.3

list3 = ["a", "b", "c", "d", "e", "f"]

random.shuffle(list3, random=myfunction)

print(list3)



