# 7. Matrix Addition & Subtraction

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result_add = [[0, 0], [0, 0]]
result_sub = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result_add[i][j] = A[i][j] + B[i][j]
        result_sub[i][j] = A[i][j] - B[i][j]

print("Addition:", result_add)
print("Subtraction:", result_sub)