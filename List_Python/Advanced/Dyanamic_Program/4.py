k = int(input("How many list wanted: "))

nested_list = []

for i in range(k):
    nested_list.append(list(map(int, input(f"Enter the element for the List{i+1} :").split())))

print("Nested list:", nested_list)

#   4.Flatten a nested list.
2
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)