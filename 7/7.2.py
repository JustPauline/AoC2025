from collections import deque

field = []
with open("data.txt") as f:
    for line in f:
        field.append(list(line.strip()))

rows = len(field)
cols = len(field[0])

for j in range(cols):
    if field[0][j] == "S":
        start = (0, j)
        break

ways = [[0] * cols for _ in range(rows)]
ways[start[0]][start[1]] = 1

queue = deque([start])
in_queue = set([start])

finished_timelines = 0

while queue:
    r, c = queue.popleft()
    in_queue.discard((r, c))

    current_ways = ways[r][c]
    if current_ways == 0:
        continue
    nr = r + 1
    nc = c

    if nr >= rows:
        finished_timelines += current_ways
        continue

    if field[nr][nc] == "^":
        produced_any = False

        li, lj = nr, nc - 1
        if lj >= 0 and field[li][lj] != "^":
            ways[li][lj] += current_ways
            produced_any = True
            if (li, lj) not in in_queue:
                queue.append((li, lj))
                in_queue.add((li, lj))

        ri, rj = nr, nc + 1
        if rj < cols and field[ri][rj] != "^":
            ways[ri][rj] += current_ways
            produced_any = True
            if (ri, rj) not in in_queue:
                queue.append((ri, rj))
                in_queue.add((ri, rj))

        if not produced_any:
            finished_timelines += current_ways

    else:
        ways[nr][nc] += current_ways
        if (nr, nc) not in in_queue:
            queue.append((nr, nc))
            in_queue.add((nr, nc))

print(finished_timelines)