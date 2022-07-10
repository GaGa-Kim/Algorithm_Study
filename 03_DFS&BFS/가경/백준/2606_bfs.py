from collections import deque

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
def bfs(graph, v, visited):
    queue = deque([v])
    # 현재 노드를 방문 처리
    visited[v] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = True
    return True

bfs(graph, 1, visited)
print(sum(visited) - 1) # 1번 컴퓨터 제외

