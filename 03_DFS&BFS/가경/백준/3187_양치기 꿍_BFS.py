from collections import deque

R, C = map(int, input().split())

# 맵 정보
graph = []
for _ in range(R):
    graph.append(list(map(str, input())))
    
# 방문 정보
visited = []
for _ in range(R):
    visited.append([0] * C)

def bfs(x, y):
    global w, s
    queue = deque()
    queue.append((x, y))

    # 현재 노드를 방문 처리
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        # 늑대일 때
        if graph[x][y] == 'v':
            w += 1

        # 양일 때
        elif graph[x][y] == 'k':
            s += 1

        for i in range(4):
            # 4가지 이동 방향에 대한 리스트 (상, 우, 하, 좌)
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            nx = x + dx[i]
            ny = y + dy[i]
            # 울타리 영역 안의 늑대와 양 수를 모두 세기
            if nx >= 0 and nx < R and ny >= 0 and ny < C:
                if graph[nx][ny] != '#' and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))

# 최종 살아남게 되는 양과 늑대의 수
wolf = 0
sheep = 0

for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and visited[i][j] == 0:
            w = 0
            s = 0
            bfs(i, j)
            if w >= s:
                s = 0
            else:
                w = 0
            wolf += w
            sheep += s

print(sheep, wolf)
