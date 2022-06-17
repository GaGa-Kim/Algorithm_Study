# 1012번
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수 출력하는 프로그램
# dfs 풀이

# 배추에 배추흰지렁이가 한 마리라도 살고 있으면 
# 상하좌우로 인접한 배추까지 보호

# 0: 배추 x, 1: 배추 o

# 재귀 limit 설정(런타임 오류 방지)
# 파이썬의 기본 재귀 한도는 1000, 재귀 깊이가 1000을 넘어갈 경우 모듈을 추가해야 함
import sys
sys.setrecursionlimit(10000)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[ny][nx] == 1:
            graph[ny][nx] = -1 # 인접한 배추 체크
            dfs(nx, ny)

# 테스트 케이스의 개수 T
t = int(input())

# 배추의 위치 X, Y 
# 0 <= X <= M-1, 0 <= Y <= N-1
for _ in range(t):
    # 배추를 심은 배추밭의 가로 길이 M, 세로 길이 N, 배추 개수 K
    # 1 <= M <= 50, 1 <= N <= 50, 1 <= K <= 2500
    m, n, k = map(int, input().split())
    graph = [ [0]*m for _ in range(n) ]
    cnt = 0

    # 배추 위치 1 표시
    for _ in range(k):
        x, y = map(int, input().split()) # (x,y) ~ (열,헹)
        graph[y][x] = 1
        
    # 배추 그룹 카운트
    for x in range(m):
        for y in range(n):
            if graph[y][x] == 1:
                dfs(x,y)
                cnt += 1
    print(cnt)
    