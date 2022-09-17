from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
distance = [0] * (100001)

def bfs(start, end):
    if end <= start:
        print(start - end)
        return
    queue = deque([start])
    while queue:
        x = queue.popleft()
        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i <= 100000 and not distance[i]:
                distance[i] = distance[x] + 1
                queue.append(i)
    print(distance[end])

bfs(n, k)
