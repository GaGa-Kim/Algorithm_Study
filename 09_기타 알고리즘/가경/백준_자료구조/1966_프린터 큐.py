from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split()))) # 문서 중요도 큐
    index = deque(list(range(n))) # 문서 인덱스 큐

    count = 0
    while queue:
        # 맨 앞의 원소가 가장 큰 값일 때
        if queue[0] == max(queue):
            count += 1
            queue.popleft()
            # 궁금한 문서와 같을 때
            if index[0] == m:
                print(count)
            index.popleft()
        # 맨 앞의 원소가 가장 큰 값이 아닐 때
        else:
            # 큐의 뒤로 보냄
            queue.append(queue.popleft())
            index.append(index.popleft())
