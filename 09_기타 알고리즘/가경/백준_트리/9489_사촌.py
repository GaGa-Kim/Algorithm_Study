from collections import defaultdict
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    # 0이 두 개 주어지면 마지막 줄
    if n == 0 and k == 0:
        break
    tree = list(map(int, input().split()))
    parent = defaultdict(int)
    index = 0
    # 루트 노드 이후 노드들의 부모 인덱스
    for i in range(1, n):
        parent[tree[i]] = tree[index]
        # +1보다 클 경우 자식이므로 인덱스 + 1
        if i < n - 1 and tree[i] + 1 < tree[i + 1]:
            index += 1
    
    # 노드의 부모의 부모가 있을 때 (루트 노드의 자식일 경우, 형제만 가능)
    if parent[parent[k]]:
        count = 0
        for i in tree:
            # 두 노드의 부모가 형제이지만, 두 노드의 부모가 다를 때 
            if (parent[parent[k]] == parent[parent[i]]) and (parent[k] != parent[i]):
                count += 1
        print(count)
    else:
        print(0)