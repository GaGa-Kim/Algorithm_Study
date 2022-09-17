from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    # A가 B를 신뢰한다 (B를 해킹하면 A도 해킹 가능)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    count = 1
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = True
    # 해킹할 수 있는 컴퓨터 수
    return count

result = []
for i in range(1, n + 1):
    result.append(bfs(i))

maxCount = max(result)
for i in range(n):
    if maxCount == result[i]:
        print(i + 1, end = ' ')