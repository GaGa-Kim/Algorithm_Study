# n x m 크기의 미로가 있을 때, 탈출하기 위해 움직여야 하는 최소 칸의 개수 구하기
# 칸을 셀 때는 시작 칸과 마지막 칸 모두 포함해서 계산
# 시작 위치는 (1,1), 출구는 (n,m), 괴물있는 칸은 0, 없는 칸은 1

from collections import deque

# 4 <= n, m <= 200
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# 이동 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 가까운 노드부터 탐색할 때는 BFS가 효율적
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인(인접 노드 확인)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# bfs 수행 결과 출력
print(bfs(0, 0))


