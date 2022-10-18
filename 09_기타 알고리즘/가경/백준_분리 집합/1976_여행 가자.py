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
# 부모 테이블 초기화
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    connect = list(map(int, input().split()))
    for j in range(1, n + 1):
        # 합집합 연산
        if connect[j - 1] == 1:
            union_parent(parent, i, j)

# 여행 계획
tour = list(map(int, input().split()))
# 여행 경로가 같은 집합인지 (루트 노드가 같은지 찾기 연산)
result = set([find_parent(parent, i) for i in tour])
if len(result) == 1:
    print("YES")
else:
    print("NO")
