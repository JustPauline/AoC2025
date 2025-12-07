field = []
with open('data.txt') as f:
    for line in f:
        field.append(list(line.strip()))

rows = len(field)
cols = len(field[0])

splitcount = 0
changed = True

counted_splits = set()

while changed:
    changed = False

    for i in range(rows):
        for j in range(cols):
            if field[i][j] in ("S", "|"):
                if i < rows - 1 and field[i+1][j] != "^" and field[i+1][j] != "|":
                    field[i+1][j] = "|"
                    changed = True

            if field[i][j] == "^":
                if (i, j) not in counted_splits:
                    if i > 0 and field[i-1][j] == "|":
                        splitcount += 1
                        counted_splits.add((i, j))

                        if j > 0 and field[i][j-1] not in ("^", "|"):
                            field[i][j-1] = "|"
                            changed = True

                        if j < cols - 1 and field[i][j+1] not in ("^", "|"):
                            field[i][j+1] = "|"
                            changed = True

print(splitcount)

