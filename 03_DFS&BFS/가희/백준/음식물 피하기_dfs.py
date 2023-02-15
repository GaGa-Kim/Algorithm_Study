# 1743번
# 통로에 떨어진 음식물 중 가장 큰 음식물의 크기 출력
# 음식물들은 인접한 것끼리 뭉쳐서 크기가 커짐
# dfs 풀이

import sys
sys.setrecursionlimit(10000)

# 세로 n, 가로 m, 음식물 개수 k
# 1 ≤ n ≤ 100 / 1 ≤ m ≤ 100 / 1 ≤ k ≤ n×m
n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0            
visited = [[False] * m for _ in range(n)]

def dfs(x, y):
    tmp = 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True  
            tmp += dfs(nx, ny)
    return tmp
            

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            tmp = dfs(i, j)
            result = max(result, tmp)
        
print(result)