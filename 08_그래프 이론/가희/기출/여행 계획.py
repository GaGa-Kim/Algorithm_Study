# 서로소 집합
# 여행지 개수와 여행지 간의 연결 정보 주어졌을 때, 
# 가능한 계획인지 여부를 판별하는 프로그램

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent(x))
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 여행지 수 n, 여행 계획에 속한 도시 수 m (1 <= n,m <= 500)
n, m = map(int, input().split())
# 부모 테이블
parent = [0] * (n+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# union 연산 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)
            
# 여행 계획
plan = list(map(int, input().split()))

result = True
# 여행 게획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False
        
if result:
    print("YES")
else:
    print("NO")