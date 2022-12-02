import sys
input = sys.stdin.readline

def dfs(node, parent):
    # 삭제될 자신의 노드는 -2로 갱신
    parent[node] = -2
    for i in range(len(parent)):
        # 부모 노드가 삭제될 경우 자식 노드도 삭제되어야 하므로 재귀적으로 방문해 부모 노드 확인
        if node == parent[i]:
            dfs(i, parent)

n = int(input())
parent = list(map(int, input().split()))
node = int(input())

dfs(node, parent)
count = 0
for i in range(len(parent)):
    # 부모 노드가 -2가 아니면서 다른 노드의 부모도 아닐 경우 
    if parent[i] != -2 and i not in parent:
        count += 1
print(count)