from collections import deque
from bisect import bisect_right

points = []
with open("data.txt") as f:
    for line in f:
        s = line.strip()
        x, y = map(int, s.split(","))
        points.append((x, y))

n = len(points)

# -------------------------
# Build compression coordinates (include x and x+1, add padding)
# Each compressed column i represents integer x in [Xs[i], Xs[i+1]-1]
# -------------------------
xs_set = set()
ys_set = set()
xs_vals = [p[0] for p in points]
ys_vals = [p[1] for p in points]
min_x = min(xs_vals); max_x = max(xs_vals)
min_y = min(ys_vals); max_y = max(ys_vals)

for x, y in points:
    xs_set.add(x)
    xs_set.add(x+1)
    ys_set.add(y)
    ys_set.add(y+1)

xs_set.add(min_x - 1)
xs_set.add(max_x + 2)
ys_set.add(min_y - 1)
ys_set.add(max_y + 2)

Xs = sorted(xs_set)
Ys = sorted(ys_set)

W = len(Xs) - 1
H = len(Ys) - 1

# widths/heights of compressed cells in real integer-tile counts
x_width = [Xs[i+1] - Xs[i] for i in range(W)]
y_height = [Ys[j+1] - Ys[j] for j in range(H)]


def x_to_c(x):
    # find i such that Xs[i] <= x < Xs[i+1], return i (0..W-1)
    return bisect_right(Xs, x) - 1


def y_to_c(y):
    return bisect_right(Ys, y) - 1


# -------------------------
# grid: 0 = unknown, 1 = boundary, 2 = exterior
# grid indexed as grid[row][col] where row 0..H-1 corresponds to Ys intervals
# -------------------------
grid = [[0] * W for _ in range(H)]

for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % n]
    if x1 == x2:
        cx = x_to_c(x1)
        cy1 = y_to_c(min(y1, y2))
        cy2 = y_to_c(max(y1, y2))
        for cy in range(cy1, cy2 + 1):
            grid[cy][cx] = 1
    elif y1 == y2:
        cy = y_to_c(y1)
        cx1 = x_to_c(min(x1, x2))
        cx2 = x_to_c(max(x1, x2))
        for cx in range(cx1, cx2 + 1):
            grid[cy][cx] = 1


# -------------------------
# Flood-fill exterior starting from the padding cell that must be outside
# Choose a cell that corresponds to (min_x-1, min_y-1)
start_cx = x_to_c(min_x - 1)
start_cy = y_to_c(min_y - 1)
q = deque()
if grid[start_cy][start_cx] == 0:
    grid[start_cy][start_cx] = 2
q.append((start_cy, start_cx))

while q:
    ry, rx = q.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny = ry + dy
        nx = rx + dx
        if 0 <= ny < H and 0 <= nx < W:
            if grid[ny][nx] == 0:
                grid[ny][nx] = 2
                q.append((ny, nx))

allowed_area = [[0] * W for _ in range(H)]
for y in range(H):
    for x in range(W):
        if grid[y][x] != 2:
            allowed_area[y][x] = x_width[x] * y_height[y]
        else:
            allowed_area[y][x] = 0

ps = [[0] * (W + 1) for _ in range(H + 1)]
for r in range(H):
    row_acc = 0
    for c in range(W):
        row_acc += allowed_area[r][c]
        ps[r+1][c+1] = ps[r][c+1] + row_acc


def rect_sum_c(cx1, cy1, cx2, cy2):
    if cx1 > cx2: cx1, cx2 = cx2, cx1
    if cy1 > cy2: cy1, cy2 = cy2, cy1
    return ps[cy2+1][cx2+1] - ps[cy1][cx2+1] - ps[cy2+1][cx1] + ps[cy1][cx1]


max_area = 0
for i in range(n):
    x1, y1 = points[i]
    cx1 = x_to_c(x1)
    cy1 = y_to_c(y1)
    for j in range(i+1, n):
        x2, y2 = points[j]
        cx2 = x_to_c(x2)
        cy2 = y_to_c(y2)

        real_w = abs(x2 - x1) + 1
        real_h = abs(y2 - y1) + 1
        needed_area = real_w * real_h

        s = rect_sum_c(cx1, cy1, cx2, cy2)
        if s == needed_area:
            if needed_area > max_area:
                max_area = needed_area

print(max_area)
