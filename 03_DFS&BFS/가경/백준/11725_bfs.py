from collections import deque
import sys
input = sys.stdin.readline

def bfs(tree, start, parent):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in tree[v]:
            if parent[i] == 0:
                parent[i] = v
                queue.append(i)

n = int(input())
# 트리 (각 노드가 연결된 정보 표현)
tree = [[] for _ in range(n + 1)]
# 부모 노드 정보
parent = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs(tree, 1, parent)

for i in range(2, n + 1):
    print(parent[i])
    

