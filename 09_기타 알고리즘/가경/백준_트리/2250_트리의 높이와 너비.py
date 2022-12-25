import sys
input = sys.stdin.readline

# 중위 순회를 돌면서 노드의 열 번호를 매겨줌
def in_order(node):
    global order
    if node:
        # 현재 노드의 왼쪽 자식, 오른쪽 자식 순으로 중위 순회하면서 열 번호를 매겨줌
        in_order(tree[node][0])
        tree[node][4] = order
        order += 1
        in_order(tree[node][1])

# 트리의 레벨(깊이) 매기기
def dfs(node, level):
    global max_level
    # 현재 노드 방문 처리
    visited[node] = True
    tree[node][3] = level
    if max_level < level:
        max_level = level
    # 현재 노드의 왼쪽 자식 노드와 오른쪽 자식 노드를 방문하지 않았다면 재귀 방문
    for i in range(2):
        if not visited[tree[node][i]]:
            dfs(tree[node][i], level + 1)

n = int(input())
# 왼쪽 자식 노드, 오른쪽 자식 노드, 부모 노드, 레벨(깊이), 열 번호
tree = [[0, 0, 0, 0, 0] for _ in range(n + 1)]
for _ in range(n):
    node, left, right = map(int, input().split())   
    # 자식이 없는 경우에는 자식 노드의 번호가 -1
    if left == -1:
        left = 0
    if right == -1:
        right = 0
    # 자식 노드와 부모 노드 기록
    tree[node][0] = left
    tree[node][1] = right
    tree[left][2] = node
    tree[right][2] = node

# 노드 방문 기록
visited = [False] * (n + 1)
visited[0] = True
# 루트 노드 찾기
root = 0
for i in range(1, n + 1):
    # 부모 노드가 0이라면 루트 노드
    if tree[i][2] == 0:
        root = i

# 중위 순회를 돌면서 노드의 열 번호를 정해줌
order = 1
in_order(root)

# 최대 레벨(깊이) 찾기
max_level = 0
dfs(root, 1)

# 각 레벨 당 너비를 구하기
level_list = [[] for _ in range(max_level + 1)]
for j in range(1, n + 1):
    level_list[tree[j][3]].append(tree[j][4])
result = []
for k in range(len(level_list)):
    # 해당 레벨에 노드가 하나라면
    if len(level_list[k]) <= 1: 
        result.append(1)
    # 해당 레벨에 노드가 두 개 이상이라면
    else:
        result.append(max(level_list[k]) - min(level_list[k]) + 1)

# 인덱스 1번부터 가장 넓은 레벨와 너비를 찾음
print(result.index(max(result), 1), max(result))
