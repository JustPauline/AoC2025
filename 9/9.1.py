points = []

with open('testdata.txt') as f:
    for line in f:
        points.append(line.strip().split(","))

areas = []
for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i+1, len(points)):
        x2, y2 = points[j]
        d = (abs((int(x2)-int(x1))) + 1) * (abs((int(y2)-int(y1))) + 1)
        areas.append(d)

areas.sort(reverse=True)
print(areas[0])