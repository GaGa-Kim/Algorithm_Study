import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# flag가 0이면 기가 노드까지의 간선 길이의 합을 구하고
# flag가 1이면 리프 노드를 돌면서 가장 긴 가지의 길이를 구함
def dfs(a, b, sum, flag):
    if flag == 0:
        # 기가 노드까지의 간선 길이의 합
        result[0] = sum
    else:
        # 긴 가지의 길이
        result[1] = max(result[1], sum)
    # 루트 노드가 기가 노드인 경우 (루트 노드 ~ 자식 노드)
    # 루트 노드가 기가 노드가 아닌 경우 (루트 노드 ~ 기가 노드 ~ 자식 노드)
    if flag == 0 and len(tree[a]) > 2 - int(a == r):
        # 기가 노드를 찾았으므로 긴 가지의 길이를 구하도록 flag를 변경하고 sum을 초기화
        flag, sum = 1, 0
    for v, d in tree[a]:
        if v == b:
            continue
        dfs(v, a, sum + d, flag)

n, r = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, d = map(int, input().split())
    tree[a].append([b, d])
    tree[b].append([a, d])
# 기둥의 길이와 가장 긴 가지의 길이
result = [0, 0]
dfs(r, r, 0, 0)
print(result[0], result[1])
