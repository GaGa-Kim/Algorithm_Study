import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    command = input().split()
    x = 0
    if len(command) == 2:
        x = command[1]
    command = command[0]

    # push X
    if command == "push":
        stack.append(x)
    # pop
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    # size
    elif command == "size":
        print(len(stack))
    # empty
    elif command == "empty":
        print(0 if len(stack) else 1)
    # top
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
