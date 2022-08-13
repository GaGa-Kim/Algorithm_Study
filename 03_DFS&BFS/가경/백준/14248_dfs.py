import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    # 왼쪽이나 오른쪽으로 이동
    for i in [-graph[v], graph[v]]:
        # 이동한 위치인 next
        next = v + i
        if next >= 0 and next < n:
            if visited[next] == 0:
                dfs(next)

n = int(input())
graph = list(map(int, input().split()))
visited = [0] * n
s = int(input())

dfs(s - 1)
print(visited.count(1))
