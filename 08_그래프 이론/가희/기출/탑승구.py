# 서로소 집합
# G개의 탑승구와 P개의 비행기가 있을 때,
# 비행기를 최대 몇 대 도킹할 수 있는 출력하는 프로그램

# 비행기가 도킹할 수 있는 탑승구의 정보 gi는 (1 <= gi <= g)
# 비행기를 1번부터 gi번째 탑승구 중 하나에 영구적으로 도킹할 수 있음을 의미
# 탑승구 하나당 비행기 한 대
# 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오면 그 시점에서 운행 중지


# 각 탑승구를 서로 다른 집합으로 나타내고, 가능한 큰 번호의 탑승구로 도킹
# 비행기가 도킹되면 해당 집합을 바로 왼쪽에 있는 집합과 union
# 단, 집합의 루트가 0이면 더 이상 도킹 불가능

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

# 1 <= g <= 100,000
g = int(input())
# 1 <= p <= 100,000
p = int(input())
# 부모 테이블
parent = [0] * (g+1)

# 자기 자신으로 부모 초기화
for i in range(1, g+1):
    parent[i] = i

result = 0
for _ in range(p):
    # 현재 비행기의 탑승구의 루트 확인
    data = find_parent(parent, int(input()))
    # 현재 루트가 0이면 운행 중지
    if data == 0:
        break
    # 바로 왼쪽 집합과 합치기
    union_parent(parent, data, data-1)
    result += 1

print(result)

