import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
crush = [[INF] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    crush[0][0] = 0
    while q:
        count, x, y = heapq.heappop(q)
        # 도착시
        if x == n - 1 and y == m - 1:
                break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and crush[nx][ny] == INF:
                # 벽인 경우
                if graph[nx][ny] == 1:
                    crush[nx][ny] = count + 1
                    heapq.heappush(q, (count + 1, nx, ny))
                # 빈 방인 경우
                else:
                    crush[nx][ny] = count
                    heapq.heappush(q, (count, nx, ny))

dijkstra()
print(crush[n - 1][m - 1])