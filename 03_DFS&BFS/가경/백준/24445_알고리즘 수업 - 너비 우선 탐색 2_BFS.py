from collections import deque
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 연결된 노드 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순
for i in range(n + 1):
    graph[i].sort(reverse=True)

# 방문 순서
count = 1
def bfs(v):
    global count
    queue = deque([v])
    visited[v] = count
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = count

bfs(r)
for i in range(n + 1):
    if i != 0:
        print(visited[i])
