from collections import defaultdict
import sys
input = sys.stdin.readline

n, w = map(int, input().split())
tree = defaultdict(int)
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u] += 1
    tree[v] += 1

leaf_count = 0
for i in range(2, n + 1):
    # 간선이 1개인 노드는 리프 노드
    if tree[i] == 1:
        leaf_count += 1

print(round(w / leaf_count, 10))
