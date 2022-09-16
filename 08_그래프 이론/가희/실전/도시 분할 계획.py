# 백준 1647번
# 크루스칼 알고리즘 (최소신장트리)
# n개의 집과 이 집들을 연결하는 m개의 길로 구성된 마을을 2개의 마을로 분할할 때, 
# 길을 없애고 남은 유지비 합의 최솟값 구하기

# 양방향, 길마다 유지 비용 있음
# 분리된 마을 안의 집들은 서로 연결되어 있어야 하고, 마을에는 집이 하나 이상 있어야 함
# 분리된 두 마을 사이 길은 없앨 수 있음

# 최소한의 비용으로 2개의 신장 트리로 분할하려면
# 크루스칼로 최소 신장 트리를 찾은 뒤, 최소 신장 트리를 구성하는 간선 중
# 가장 비용이 큰 간선을 제거하면 됨

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드 찾을 때까지 재귀적 호출
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
        
# 노드 개수, 간선(union 연산) 개수
# 2 <= n <= 100,000 / 1 <= m <= 1,000,000
n, m = map(int, input().split())
# 부모 테이블
parent = [0] * (n+1)

edges = [] # 모든 간선 리스트
result = 0 # 최종 비용

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i
    
# 모든 간선 정보
for _ in range(m):
    # a번 집과 b번 집을 연결하는 길의 유지비 c (1 <= c <= 1,000)
    a, b, c = map(int, input().split())
    # 비용순으로 정렬하기 위해 튜플의 첫 번재 원소를 비용으로 설정
    edges.append((c, a, b))
    
# 간선 비용순 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간서
last = 0

# 간선 하나씩 확인하며
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last)
