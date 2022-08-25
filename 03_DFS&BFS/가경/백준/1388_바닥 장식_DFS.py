n, m = map(int, input().split())

# 맵 정보
graph = []
for _ in range(n):
    graph.append(list(input()))

# 방문 정보
visited = []
for _ in range(n):
    visited.append([False] * m)

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 이미 방문한 곳은 가지 않음
    if visited[x][y] == True:
        return False
    # 위의 2가지 경우가 아니라면 현재 위치 방문 처리한 후
    visited[x][y] = True
    # 현재 index의 모양이 '-'이고 다음 오른쪽 칸의 모양이 '-'이거나
    # 현재 index의 모양이 '-'이고 현재 index가 마지막 칸이면
    if graph[x][y] == '-' and (y == m - 1 or graph[x][y + 1] == '-'):
        dfs(x, y + 1) # 오른쪽으로 이동하고
    # 현재 index의 모양이 '|'이고 다음 아래 칸의 모양이 '|'이거나
    # 현재 index의 모양이 '|'이고 현재 index가 마지막 칸이면
    elif graph[x][y] == '|' and (x == n - 1 or graph[x + 1][y] == '|'):
        dfs(x + 1, y) # 아래쪽으로 이동
    return True
    
count = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y) == True:
            count += 1
            
print(count)