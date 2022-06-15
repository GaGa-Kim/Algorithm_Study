# 백준 14502번
# 안전 영역 크기의 최댓값을 구하는 프로그램

# 연구소 N*M 직사각형, 1*1 크기의 정사각형으로 구성

# 바이러스는 상하좌우 인접한 빈 칸으로 퍼져나감

# 새로 세울 수 있는 벽의 개수 3개(필수)
# 벽 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳 = 안전영역


# 벽의 개수가 3개가 되는 모든 조합 계산
# -> 각 조합에 대해 안전 영역 크기 계산
# => DFS/BFS + 완전탐색 + 구현

# 지도 세로 N, 가로 M (3<=N, M<=8)
n, m = map(int, input().split())

# 지도 모양
# 0: 빈 칸, 1: 벽, 2: 바이러스
data = []  # 초기 지도
temp = [[0] * m for _ in range(n)] # 벽 설치 뒤 지도

for _ in range(n):
    data.append(list(map(int, input().split())))
    
# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색 이용 ~> 바이러스가 사방으로 퍼지도록
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상하좌우 중 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치, 재귀 수행
                temp[nx][ny] = 2
                virus(nx, ny)


# 현재 맵에서 안전영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


# 깊이 우선 탐색 이용해 벽 설치 + 안전 영역 크기 계산
def dfs(count):
    global result
    # 벽 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for i in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
                    
        # 안전 영역의 최댓값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 벽 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)