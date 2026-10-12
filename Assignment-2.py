from collections import deque

def maxRegion(grid):
    rows = len(grid)
    cols = len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    largest = 0

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 1 and not visited[i][j]:

                queue = deque([(i, j)])
                visited[i][j] = True
                count = 0

                while queue:
                    r, c = queue.popleft()
                    count += 1

                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc

                        if (0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == 1 and
                            not visited[nr][nc]):

                            visited[nr][nc] = True
                            queue.append((nr, nc))

                largest = max(largest, count)

    return largest


rows = int(input())
cols = int(input())

grid = []

for _ in range(rows):
    grid.append(list(map(int, input().split())))

print(maxRegion(grid))
