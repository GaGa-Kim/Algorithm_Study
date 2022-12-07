import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0] * (n + 1) # 부모 노드 정보
    # 부모 노드 정보 저장
    for _ in range(n - 1):
        a, b = map(int, input().split())
        parent[b] = a

    i, j = map(int, input().split())
    i_parent = [i]
    j_parent = [j]
    # 각 노드의 부모 노드가 루트일 때까지 모두 저장
    while parent[i]:
        i_parent.append(parent[i])
        i = parent[i]
    while parent[j]:
        j_parent.append(parent[j])
        j = parent[j]

    # 같은 레벨이면서 부모 노드가 같은 것을 찾기
    i_level = len(i_parent) - 1
    j_level = len(j_parent) - 1
    while i_parent[i_level] == j_parent[j_level]:
        i_level -= 1
        j_level -= 1
    print(i_parent[i_level + 1])