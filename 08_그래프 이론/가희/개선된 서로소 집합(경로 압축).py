# 최악의 경우 전체 시간 복잡도 O(VM)될 수 있음
# ~> 경로 압축을 통해 find 함수를 최적화할 수 있다
# ~> 노드 V개, union 연산 V-1개, find 연산 M개 일 때 
#       => O(V + M(1 + log2-M/V V))

# 경로 압축) find 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 갱신하는 기법

# 특정 원소가 속한 집합 찾기(경로 압축 기법 이용)
def find_parent(parent, x):
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
        
# 노드의 개수와 간선(union 연산)의 개수
v, e = map(int, input().split())
# 부모 테이블
parent = [0] * (v+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# union 연산 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ') # 1 1 1 1 5 5

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ') # 1 1 1 1 5 5