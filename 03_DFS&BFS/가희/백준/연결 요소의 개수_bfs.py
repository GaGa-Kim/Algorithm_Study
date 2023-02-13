# 11724번
# 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램
# bfs 풀이

from collections import deque
import sys
input = sys.stdin.readline

# 정점 개수 n, 간선 개수 m
# 1 ≤ N ≤ 1,000 / 0 ≤ M ≤ N×(N-1)/2
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    # 간선의 양 끝점 u, v
    # 1 ≤ u,v ≤ N / u ≠ v
    u, v = map(int, input().split())    
    graph[u].append(v)
    graph[v].append(u)


result = 0
visited = [False] * (n+1)

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                
result = 0
for i in range(1, n+1):
    if not visited[i]:
        result += 1
        bfs(i)

print(result)