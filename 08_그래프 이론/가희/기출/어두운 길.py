# 크루스칼 (최소 신장 트리)
# n개의 집과 m개의 도로로 구성된 마을에서 특정 도로의 가로등을 비활성하여
# 절약할 수 있는 최대 금액을 출력하는 프로그램

# 특정 도로의 가로등 비용은 해당 도로의 길이와 동일

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트노드가 아니라면 루트노드 찾을 때까지 재귀 호출
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

# 1 <= n <= 200,000 / n-1 <= m <= 200,000
n, m = map(int, input().split())
# 부모 테이블
parent = [0] * (n+1)

# 모든 간선 리스트
edges = []
# 전체 비용과 최종 비용
total = result = 0

# 자기 자신으로 부모 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선 정보
for _ in range(m):
    # x번 집과 y번 집 사이 양방향 도로 존재, 그 길이가 z (0 <= x,y < n)
    x, y, z = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((z, x, y))
    
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    z, x, y = edge
    total += z
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z

print(total - result)


