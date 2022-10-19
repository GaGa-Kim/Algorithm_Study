import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선을 비용순으로 오름차순 정렬
edges.sort()

for cost, a, b in edges:
    # 사이클이 발생하지 않을 경우 (같은 집합이 아니라면)
    if find_parent(parent, a) != find_parent(parent, b):
        # 해당 간선을 최소 신장 트리 집합에 포함
        union_parent(parent, a, b)
        result += cost

print(result)
