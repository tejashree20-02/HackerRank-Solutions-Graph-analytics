import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

edges = [dict() for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges[u][v] = w

q = int(input())

queries = []
sources = {}

for _ in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    queries.append((a, b))

    if a not in sources:
        sources[a] = set()
    sources[a].add(b)

graph = [[] for _ in range(n)]

for u in range(n):
    for v, w in edges[u].items():
        graph[u].append((v, w))

INF = 10**18
answers = {}

for start, targets in sources.items():

    dist = [INF] * n
    dist[start] = 0

    heap = [(0, start)]
    remaining = len(targets)

    while heap and remaining > 0:
        d, u = heapq.heappop(heap)

        if d != dist[u]:
            continue

        if u in targets:
            remaining -= 1
            targets.remove(u)

        for v, w in graph[u]:
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    for _, b in [x for x in queries if x[0] == start]:
        answers[(start, b)] = -1 if dist[b] == INF else dist[b]

out = []

for a, b in queries:
    out.append(str(answers[(a, b)]))

sys.stdout.write("\n".join(out))
