import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

# 연결된 노드 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 오름차순
for i in range(n + 1):
    graph[i].sort()

# 방문 순서
count = 1
def dfs(v):
    global count
    visited[v] = count
    for i in graph[v]:
        if not visited[i]:
            count += 1
            dfs(i)

dfs(r)
for i in range(n + 1):
    if i != 0:
        print(visited[i])
