n = int(input())
m = int(input())

# 각 노드가 연결된 정보를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 각 노드가 방문된 정보를 표현 (0 ~ n)
visited = [0] * (n + 1)

count = 0
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = 1
    # 현재 노드와 연결된 다른 도르를 재귀적으로 방문
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return True

dfs(graph, 1, visited)
print(sum(visited) - 1) # 1번 컴퓨터 제외

