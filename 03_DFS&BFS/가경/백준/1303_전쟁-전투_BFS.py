from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y, color):
    queue = deque()
    queue.append((x, y))
    global count
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == color and graph[nx][ny] != 0:
                count += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return (1 if count == 0 else count)

white_count, blue_count = 0, 0
for i in range(m):
    for j in range(n):
        count = 0
        if graph[i][j] != 0:
            if graph[i][j] == 'W':
                white_count += bfs(i, j, 'W') ** 2
            elif graph[i][j] == 'B':
                blue_count += bfs(i, j, 'B') ** 2
print(white_count, blue_count)  