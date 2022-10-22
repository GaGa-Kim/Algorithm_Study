from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
for i in range(1, n + 1):
    queue.append(i)

result = []
while queue:
    for _ in range(k - 1):
        # k - 1 번째 전까지 queue에서 pop한 후 다시 append (원이므로 다시 뒤로 넣어줌)
        queue.append(queue.popleft())
    # k번째 사람일 경우 queue에서 pop한 후 result에 append (제거)
    result.append(queue.popleft())

print(str(result).replace('[', '<').replace(']', '>'))