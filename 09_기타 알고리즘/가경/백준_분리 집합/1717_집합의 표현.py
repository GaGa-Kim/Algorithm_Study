import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

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

n, m = map(int, input().split())
# 부모 테이블 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    cal, a, b = map(int, input().split())
    # 합집합 연산
    if cal == 0:
        union_parent(parent, a, b)
    # 찾기 연산
    elif cal == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
