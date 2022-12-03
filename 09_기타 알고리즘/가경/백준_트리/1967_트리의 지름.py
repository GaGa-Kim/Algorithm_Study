import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(start, cost):
    # 현재 노드와 연결된 노드의 가중치를 확인
    for x, y in tree[start]:
        # 방문하지 않은 노드라면
        if distance[x] == -1:
            # 이전 노드의 가중치와 현재 노드의 가중치를 합함
            distance[x] = cost + y
            # 재귀적으로 연결된 노드 탐색
            dfs(x, cost + y)

n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

# 첫 번째 노드에서 제일 먼 노드 찾기
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
node = distance.index(max(distance))

# 제일 먼 노드에서 다시 가장 제일 먼 노드 찾기
distance = [-1] * (n + 1)
distance[node] = 0
dfs(node, 0)

print(max(distance))