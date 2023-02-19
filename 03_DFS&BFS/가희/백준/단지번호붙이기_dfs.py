# 2667번
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를
# 오름차순으로 정렬하여 출력하는 프로그램
# dfs 풀이

# 지도 크기 n x n (5 ≤ N ≤ 25)
n = int(input())

graph = [list(map(int,input())) for _ in range(n)] 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    tmp = 1
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == 1:
            tmp += dfs(nx, ny)
    return tmp

visited = [[False] * n for _ in range(n)]
result = 0
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result += 1
            tmp = dfs(i, j)
            houses.append(tmp)

print(result)
houses.sort()
print(*houses, sep='\n')
