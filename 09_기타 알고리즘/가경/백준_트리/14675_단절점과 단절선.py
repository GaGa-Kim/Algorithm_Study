import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)] # 노드 (정점)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    # 단절점인지 판별
    if t == 1:
        # 리프 노드가 아닐 경우 단절점
        if len(tree[k]) <= 1:
            print("no")
        else:
            print("yes")
    # 단절선인지 판별
    else:
        # 트리이므로 모든 간선은 단절선
        print("yes")
