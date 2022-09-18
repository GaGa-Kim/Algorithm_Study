import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    global size
    if x < 0 or x >= n or y < 0 or y >= m:
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

nums = 0
result = 0
for i in range(n):
    for j in range(m):
        size = 0
        if dfs(i, j):
            nums += 1
            result = max(result, size)
print(nums)
print(result)