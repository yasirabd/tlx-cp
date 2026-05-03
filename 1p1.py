n, m, x = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
operations = []
for _ in range(x):
    operations.append(input().strip())

def matrix_operation(matrix, operation):
    if operation == "_": # horizontal flip
        return matrix[::-1]
    elif operation == "|": # vertical flip
        return [row[::-1] for row in matrix]
    elif operation == "90": # 90 degree clockwise rotation
        return [list(row[::-1]) for row in zip(*matrix)]
    elif operation == "180": # 180 degree clockwise rotation
        return [row[::-1] for row in matrix[::-1]]
    elif operation == "270": # 270 degree clockwise rotation
        m = list(zip(*matrix))[::-1]
        return [list(row) for row in m]

for op in operations:
    matrix = matrix_operation(matrix, op)

# print the final matrix
for row in matrix:
    print(*row)