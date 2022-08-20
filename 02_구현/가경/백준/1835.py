from collections import deque

n = int(input())
queue = deque()
queue.append(n)

# 역순으로 수행해서 배열에 저장
# n - 1부터 -1 숫자만큼의 간격으로 0까지의 범위 저장
for i in range(n - 1, 0, -1):
    queue.appendleft(i)
    for j in range(i):
        queue.appendleft(queue.pop())

print(*queue)