import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, k = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r][c] = 1

def dfs(x, y):
    global size
    if x < 0 or x > n or y < 0 or y > m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        size += 1
        dfs(x - 1, y) 
        dfs(x, y - 1) 
        dfs(x + 1, y) 
        dfs(x, y + 1) 
        return True
    return False

result = 0
for i in range(n + 1):
    for j in range(m + 1):
        size = 0
        if dfs(i, j):
            result = max(result, size)
print(result)