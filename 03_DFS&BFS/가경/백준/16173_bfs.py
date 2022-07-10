from collections import deque

n = int(input())

# 맵 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 정보
visited = []
for _ in range(n):
    visited.append([False] * n)

# 이동할 두 가지 방향 정의 (우, 하)
dx = [0, 1]
dy = [1, 0]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # -1이라면 가장 아래 칸에 도달한 것
        if graph[x][y] == -1:
            return 'HaruHaru'
        # 현재 위치에서 2가지(우, 하) 위치 각각 확인
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            # 외부로는 가지 않음
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 이미 방문한 곳은 가지 않음
            if visited[nx][ny] == True:
                continue
            # 위의 3가지 경우가 아니라면 방문 처리한 후
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                # 큐에 넣어줌
                queue.append((nx, ny))
    return 'Hing'

print(bfs(0, 0, visited))