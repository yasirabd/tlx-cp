n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# transpose
transpose = list(zip(*matrix))

# reverse each row and print
for row in transpose:
    print(*row[::-1])