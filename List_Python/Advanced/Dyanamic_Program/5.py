k = int(input("Enter the number of rows & columns: "))

matrix = []

for i in range(k):
    row = list(input(f"Enter the element of row{i+1}: ").split())
    matrix.append(row)

print("Matrix:", matrix)

#   5.Create a matrix using lists and access specific rows and columns.

row = int(input("Which Row is wanted to be print: "))

if row <= len(matrix):
    print("Row", row, " :", matrix[row-1])
else:
    print("Invalid Row number")

col = int(input("Which Column is wanted to be print: "))

if col <= len(matrix[0]):
    print("Column", col, " :", [row[col-1] for row in matrix])
else:
    print("Invalid Column number")

r,c = list(map(int, input("Enter the row & column number: ").split()))

if r <= len(matrix) and c <= len(matrix[0]):
    print("Element at Row", r, "and Column", c, "is:", matrix[r-1][c-1])
else:
    print("Invalid Row or Column number")
