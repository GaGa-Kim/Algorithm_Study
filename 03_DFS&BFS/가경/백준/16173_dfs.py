n = int(input())

# 맵 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 정보
visited = []
for _ in range(n):
    visited.append([False] * n)

# 이동할 두 가지 방향 정의 (우, 하)
dx = [0, 1]
dy = [1, 0]

def dfs(x, y, visited):
    # 외부로는 가지 않음
    if x <= -1 or x >= n or y <= -1 or y >= n: 
        return False
    # 이미 방문한 곳은 가지 않음
    if visited[x][y] == True: 
        return False
    # -1이라면 가장 아래 칸에 도달한 것
    if graph[x][y] == -1:
        print('HaruHaru')
        exit()
    # 위의 3가지 경우가 아니라면 방문 처리한 후
    visited[x][y] = True
    # 현재 위치에서 2가지(우, 하) 위치 각각 확인 
    for i in range(2):
        nx = x + dx[i] * graph[x][y]
        ny = y + dy[i] * graph[x][y]
        dfs(nx, ny, visited)
    return 'Hing'

print(dfs(0, 0, visited))
    
