def journeyToMoon(n, astronaut):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[b] = a

    for a, b in astronaut:
        union(a, b)

    country_size = {}

    for i in range(n):
        root = find(i)
        country_size[root] = country_size.get(root, 0) + 1

    answer = 0
    total = 0

    for size in country_size.values():
        answer += size * total
        total += size

    return answer

n, p = map(int, input().split())

astronaut = []

for _ in range(p):
    a, b = map(int, input().split())
    astronaut.append([a, b])

print(journeyToMoon(n, astronaut))
