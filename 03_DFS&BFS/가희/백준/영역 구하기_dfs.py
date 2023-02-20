# 2583번
# 세로 m, 가로 n 그리고 k개의 직사각형의 좌표가 주어질 때, 
# k개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 
# 그리고 분리된 각 영역의 넓이가 얼마인지 구하는 프로그램
# dfs 풀이

import sys
sys.setrecursionlimit(100000)

# m, n, k ≤ 100 
m, n, k = map(int, input().split())

visited = [[False] * n for _ in range(m)]  

graph = [[0] * n for _ in range(m)]
for _ in range(k):
    # 왼쪽 아래 꼭짓점의 (x,y), 오른쪽 위 꼭짓점의 (x,y)
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            visited[i][j] = True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    tmp = 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
            tmp += dfs(nx, ny)
    return tmp

area = []
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            tmp = dfs(i, j)
            area.append(tmp);

print(len(area))
print(*sorted(area))