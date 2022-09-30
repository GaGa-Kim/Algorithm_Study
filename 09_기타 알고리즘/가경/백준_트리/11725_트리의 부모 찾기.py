import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start):
    # 현재 트리 노드와 연결된 다른 노드를 재귀적으로 방문해 부모 노드 확인
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i)

n = int(input())
# 트리 (각 노드가 연결된 정보 표현)
tree = [[] for _ in range(n + 1)]
# 부모 노드 정보
parent = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
for i in range(2, n + 1):
    print(parent[i])