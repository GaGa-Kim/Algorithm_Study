# 서로소 집합 문제
# m개의 연산을 수행할 때, '같은 팀 여부 확인' 연산에 대한 연산 결과 출력하는 프로그램

# 1. 팀 합치기) 두 팀 합치는 연산 (0)
# 2. 같은 팀 여부 확인) 특정 두 학생이 같은 팀에 속하는지 확인하는 연산 (1)

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
        
# 1 <= n,m <= 100,000   ~> 경로 압축으로 시간복잡도 개선
n, m = map(int, input().split())
# 부모 테이블
parent = [0] * (n+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i
    
# 각 연산 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')