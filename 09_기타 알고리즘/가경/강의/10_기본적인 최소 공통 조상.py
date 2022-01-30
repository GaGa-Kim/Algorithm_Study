# 10_기본적인 최소 공통 조상.py
import sys
sys.setrecursionlimit(int(1e5)) # 런타임 오류를 피하기
n = int(input())

parent = [0] * (n + 1) # 부모 노드 정보
d = [0] * (n + 1) # 각 노드까지의 깊이
c = [0] * (n + 1) # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n + 1)] # 그래프 정보

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 각각의 노드에 대한 깊이를 구하는 함수
def dfs(x, depth):
    c[x] = True
    d[x] = depth
    for y in graph[x]: # 그래프 정보를 보며 (연결된 노드 정보)
        if c[y]: # 인접한 노드가 이미 깊이를 구했다면 넘기기
            continue
        parent[y] = x # 인접한 노드의 깊이가 구해져 있지 않다면 그 노드의 부모 노드를 자신(x)으로 정해주기
        dfs(y, depth + 1) # 인접한 노드에 대해서 현재까지의 노드 깊이 + 1를 깊이로 대입

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # 먼저 깊이가 동일하도록
    while d[a] != d[b]:
        if d[a] > d[b]: # 더 깊이가 큰 쪽 (밑 쪽의 노드)이 부모 쪽으로 이동하여 깊이가 동일하도록
            a = parent[a]
        else:
            b = parent[b]
    # 깊이가 동일하면 노드가 같아지도록 부모 방향으로 이동 이동
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

dfs(1, 0) # 루트 노드는 1번 노드

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))