from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 현재 노드를 방문 처리
    graph[x][y] = 2
    while queue:
        x, y = queue.popleft()
        for i in range(4): 
            # 4가지 이동 방향
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
        
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                # 전류가 통할 경우만 탐색 가능
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    queue.append((nx, ny))

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().strip())))

# outer side 부분인 첫 줄만 dfs 탐색
for i in range(n):
    if graph[0][i] == 0:
        bfs(0, i)

# inner side 부분인 마지막 줄에 2(방문 처리)가 있다면 전달 성공
print("YES" if 2 in graph[-1] else "NO")