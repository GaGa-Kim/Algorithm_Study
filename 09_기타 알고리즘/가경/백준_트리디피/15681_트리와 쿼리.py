import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# dfs로 탐색하면서 각 정점에 대한 서브 트리 수 구하기
def countPoint(x):
    # 현재 노드 방문
    count[x] = 1
    # 현재 노드와 연결된 다른 노드(자식)를 재귀적으로 방문
    for i in tree[x]:
        if not count[i]:
            countPoint(i)
            count[x] += count[i]

n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
count = [0] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

countPoint(r)

for _ in range(q):
    u = int(input())
    print(count[u])
