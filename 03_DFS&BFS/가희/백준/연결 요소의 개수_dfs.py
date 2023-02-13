# 11724번
# 방향 없는 그래프가 주어졌을 때, 연결 요소의 개수를 구하는 프로그램
# dfs 풀이

import sys
sys.setrecursionlimit(10000)
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
    
visited = [False] * (n+1)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

result = 0
for i in range(1, n+1):
    if not visited[i]:
        result += 1
        dfs(i)

print(result)