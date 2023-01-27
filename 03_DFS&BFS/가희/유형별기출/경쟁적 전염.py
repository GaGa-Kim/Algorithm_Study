# 백준 18405번 (bfs)
# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, 
# s초가 지난 후 (x,y)에 존재하는 바이러스의 종류를 출력하는 프로그램
# (바이러스가 없으면 0 출력)

# 시험관 크기 n x n, 바이러스의 종류는 1 ~ k번까지 k가지
# 바이러스는 1초마다 상하좌우 방향으로 증식(낮은 번호부터 증식)
# 특정 칸에 이미 바이러스 있으면 다른 바이러스 못들어감

from collections import deque

# 1 <= n <= 200, 1 <= k <= 1,000
n, k = map(int, input().split())

# 시험관 정보, 바이러스 없는 칸은 0
graph = []  # 전체 보드 정보
data = []   # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, 위치 y) 삽입
            data.append((graph[i][j], 0, i, j))

# 오름차순으로 정렬 후 큐로 옮기기
data.sort()
q = deque(data)

# 0 <= s <= 10,000, 1 <= x,y <= n
target_s, target_x, target_y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 방향 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])
