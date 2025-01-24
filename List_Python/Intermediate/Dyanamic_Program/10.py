list1 = list(map(int, input("Enter the Frist List: ").split()))

#   10.Replace all occurrences of a specific value in a list with another value.

replace_value = int(input("Enter the value for replace: "))
new_value = int(input("Enter the new value: "))

found = False

for element in range(len(list1)):
    if list1[element] == replace_value:
        list1[element] = new_value
        found = True
    
if not found:
    print("The Replace value was not found in the list.")
else:
    print("List after replacing:", list1)