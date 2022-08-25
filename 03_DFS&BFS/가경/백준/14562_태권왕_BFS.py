from collections import deque
import sys
input = sys.stdin.readline

def bfs(s, t):
    queue = deque()
    queue.append((s, t, 0))
    while queue:
        s, t, n = queue.popleft()
        if s < t:
            # 이길 경우 현재 점수만큼 점수를 얻고, 질 경우 상대에게 3점을 줌
            queue.append((s * 2, t + 3, n + 1))
            # 이길 경우 1점을 얻음
            queue.append((s + 1, t, n + 1))
        elif s == t:
            print(n)
            break

for _ in range(int(input())):
    s, t = map(int, input().split())
    bfs(s, t)
