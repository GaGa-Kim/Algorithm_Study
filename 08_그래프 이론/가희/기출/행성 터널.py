# 백준 2887번 / 크루스칼 (최소신장트리)
# n개의 행성이 있을 때 터널을 n-1개 건설하여 모든 행성이 서로 연결되게 하려고 할 때,
# 모든 행성을 터널로 연결하는데 필요한 최소 비용 구하는 프로그램

# 두 행성 A(xa, ya, za)와 B(xb, yb, zb)를 터널로 연결할 때
# 드는 비용은 min( |xa-xb|, |ya-yb|, |za-zb| )

# 모든 두 행성 간의 거리 확인하는 방법 -> 시간 초과
# 1. 입력 받은 뒤 x축, y축, z축을 기준으로 각각 정렬하고
# 2. 각각 n-1개의 간선만 고려해도 총 간선의 개수 3(n-1)개로 해결 가능 

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 1 <= n <= 100,000
n = int(input())
# 부모 테이블
parent = [0] * (n+1)

# 모든 간선 리스트
edges = []
# 최종 비용
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드에 대한 좌표 값 입력받기
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보 추출하여 처리
for i in range(n-1):
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))
    

# 간선을 비용순으로 정렬
edges.sort()

# 간선 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a , b)
        result += cost
        
print(result)