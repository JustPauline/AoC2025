matrix = []
total = 0
data = []

with open('data.txt') as f:
    for line in f:
        line.split(" ")
        matrix.append(line)

rows = len(matrix)
cols = len(matrix[0])

operators = matrix[-1]
operators = operators.strip().split()

for i in range(cols):
    column_values = [matrix[j][i] for j in range(rows - 1)]

    data.append(column_values)


def is_separator(column):
    return all(ch == " " for ch in column)


current_equation = []
i = 0

for rij in data:
    if not is_separator(rij) and "\n" not in rij:
        digits = [ch for ch in rij if ch != " "]
        number = int("".join(digits))
        current_equation.append(number)
    else:
        if operators[i] == "*":
            answer = 1
            for v in current_equation:
                answer *= v

        if operators[i] == "+":
            answer = 0
            for v in current_equation:
                answer += v
        current_equation = []
        i += 1
        total += answer
print(total)