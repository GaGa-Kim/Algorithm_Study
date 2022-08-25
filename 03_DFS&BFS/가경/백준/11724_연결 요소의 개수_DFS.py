import sys
sys.setrecursionlimit(10000)  

n, m = map(int,sys.stdin.readline().split())

# 맵 정보
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 처리
visited = [False] * (n + 1)

# 연결 요소의 개수
count = 0 

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

for i in range(1, n + 1):
    if not visited[i]:
        # 해당 정점에 연결된 그래프가 없다면
        if not graph[i]:
            count += 1
            visited[i] = True
        # 해당 정점에 연결된 그래프가 있다면
        else: 
            dfs(graph, i, visited)
            count += 1
print(count)
        