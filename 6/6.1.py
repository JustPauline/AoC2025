matrix = []
total = 0

with open('data.txt') as f:
    for line in f:
        matrix.append(line.strip().split())

rows = len(matrix)
cols = len(matrix[0])

for i in range(cols):
    column_values = [int(matrix[j][i]) for j in range(rows - 1)]
    answer = 0

    if matrix[-1][i] == "*":
        answer = 1
        for v in column_values:
            answer *= v

    elif matrix[-1][i] == "+":
        for v in column_values:
            answer += v

    total += answer

print(total)
