import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start):
    global leaf_count
    visited[start] = 1
    # 간선이 1개인 노드는 리프 노드
    if (len(tree[start]) == 1) and (visited[tree[start][0]] == 1):
        leaf_count += 1
    for i in tree[start]:
        if visited[i] == 0:
            dfs(i)

n, w = map(int, input().split())
tree = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

leaf_count = 0
dfs(1)

print(round(w / leaf_count, 10))
