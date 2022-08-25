from collections import deque

def bfs(graph, a, b):
    # 4가지 이동 방향에 대한 리스트 (상, 우, 하, 좌)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((a, b))
    graph[a][b] = 2

    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우 중에서 지렁이가 지나갈 수 있는 곳
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))

T = int(input())
for _ in range(T):
    # 맵 정보
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                count += 1

    print(count)