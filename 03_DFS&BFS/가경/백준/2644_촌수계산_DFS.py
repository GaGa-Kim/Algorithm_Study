n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

# 각 노드가 연결된 정보를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 각 노드가 방문된 정보를 표현 (0 ~ n)
visited = [0] * (n + 1)
# 촌수 정보
result = [0] * (n + 1)

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            # v와의 촌수 정보 업데이트 
            result[i] = result[v] + 1
            dfs(graph, i, visited)

dfs(graph, p1, visited)

# p1이 촌수 정보를 모두 업데이트한 후, p1와 p2의 촌수 정보 출력
if result[p2] > 0:
    print(result[p2])
else:
    print(-1)