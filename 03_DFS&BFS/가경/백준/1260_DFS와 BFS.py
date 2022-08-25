from collections import deque

n, m, v = map(int, input().split())

# 각 노드가 연결된 정보를 표현
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 작은 노드부터 방문하도록 그래프 정렬
for i in range(len(graph)):
    graph[i].sort()

# 각 노드가 방문된 정보를 표현 (0 ~ n)
visited1 = [0] * (n + 1)
visited2 = [0] * (n + 1)

def dfs(graph, v, visited1):
    # 현재 노드를 방문 처리
    visited1[v] = 1
    print(v, end= ' ')
    # 현재 노드와 연결된 다른 도르를 재귀적으로 방문
    for i in graph[v]:
        if visited1[i] == 0:
            dfs(graph, i, visited1)
    return True

def bfs(graph, v, visited2):
    queue = deque([v])
    # 현재 노드를 방문 처리
    visited2[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        print(v, end= ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if visited2[i] == 0:
                queue.append(i)
                visited2[i] = True
    return True

dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)