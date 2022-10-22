from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    command = input().split()
    x = 0
    if len(command) == 2:
        x = command[1]
    command = command[0]

    # push_front X
    if command == "push_front":
        queue.appendleft(x)
    # push_back X
    elif command == "push_back":
        queue.append(x)
    # pop_front
    elif command == "pop_front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    # pop_back
    elif command == "pop_back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
            queue.pop()
    # size
    elif command == "size":
        print(len(queue))
    # empty
    elif command == "empty":
        print(0 if len(queue) else 1)
    # front
    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    # back
    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
