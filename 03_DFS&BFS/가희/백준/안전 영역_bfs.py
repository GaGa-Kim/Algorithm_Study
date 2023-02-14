# 2468번
# 어떤 지역의 높이 정보가 주어졌을 때, 
# 장마철에 물에 잠기지 않는 영역의 최대 개수를 계산하는 프로그램
# bfs 풀이

# 안전 영역
# : 상하좌우에 물에 잠기는 지점이 없고, 그 크기가 최대인 영역

from collections import deque

#  2 <= n <= 100
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

dx = [-1, 0, 1, 0]             
dy = [0, 1, 0, -1]

def bfs(x, y, h):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                
result = 1
maxH = max(map(max, graph))
for k in range(maxH):
    visited = [[False] * n for _ in range(n)]
    tmp = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                tmp += 1
                visited[i][j] = True
                bfs(i, j, k)
    result = max(result, tmp)

print(result)