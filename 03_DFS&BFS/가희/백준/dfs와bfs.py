# 백준 1260번
# 그래프를 dfs로 탐색한 결과와 bfs로 탐색한 결과를 출력하는 프로그램

# 단, 방문할 수 있는 정점이 여러 개인 경우 
# 정점 번호가 작은 것부터 방문, => sort()로 정렬해줘야 함
# 더 이상 방문할 수 있는 점 없으면 종료

import sys
input = sys.stdin.readline
from collections import deque

# 정점 개수 N, 간선 개수 M, 시작 정점 V
# 1 <= N <= 1000, 1 <= M <= 10000
n, m, v = map(int, input().split())

# 정점 연결 정보
# ( 두 정점 사이 여러 개 간선 o, 양방향 )
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  

#print(graph)
# 작은 노드부터 방문해야 하므로 
# 각 간선 정보에 대해 모두 정렬
for i in range(1, n+1):
    graph[i].sort()
#print(graph)

def dfs(v):
    print(v, end=' ')
    visited_dfs[v] = True
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)
            visited_dfs[i]=True
            
def bfs(v):
    q = deque([v]) 
    visited_bfs[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited_bfs[i]:
                q.append(i)
                visited_bfs[i] = True
    

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

dfs(v)
print()
bfs(v)