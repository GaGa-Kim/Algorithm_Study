from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 현재 노드를 방문 처리 (섬에서 바다로)
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            # 8가지 이동 방향에 대한 리스트 (상, 하, 좌, 우, 상우, 상좌, 우하, 우좌)
            dx = [1, 1, -1, -1, 1, -1, 0, 0]
            dy = [0, 1, 0, 1, -1, -1, 1, -1]
        
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < h and ny >= 0 and ny < w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # 맵 정보
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    # 섬의 갯수
    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                count += 1
    print(count)