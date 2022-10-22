from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

for _ in range(n - 1):
    # 제일 위에 있는 카드를 버림
    queue.popleft()
    # 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
    queue.append(queue.popleft())
print(queue[-1])