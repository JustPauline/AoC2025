points = []

with open('data.txt') as f:
    for line in f:
        points.append(line.strip().split(","))

edges = []
for i in range(len(points)):
    x1, y1, z1 = points[i]
    for j in range(i+1, len(points)):
        x2, y2, z2 = points[j]
        d = (int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + (int(z1)-int(z2))**2
        edges.append((d, i, j))

edges.sort()


class DSU: # met dank aan het internet
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  # already in same group
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra  # ensure ra is larger
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self):
        # Count sizes of root nodes only
        roots = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            roots[r] = roots.get(r, 0) + 1
        return list(roots.values())


dsu = DSU(len(points))

for k in range(1000):
    d, i, j = edges[k]
    dsu.union(i, j)

sizes = dsu.component_sizes()
sizes_sorted = sorted(sizes, reverse=True)

answer = sizes_sorted[0] * sizes_sorted[1] * sizes_sorted[2]
print(answer)
