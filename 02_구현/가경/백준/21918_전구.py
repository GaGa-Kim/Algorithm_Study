import sys
input = sys.stdin.readline

n, m = map(int, input().split())
light = list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    # 1번 명령어
    if a == 1:
        light[b - 1] = c
    # 2번 명령어
    elif a == 2:
        for i in range(b - 1, c):
            if light[i] == 0:
                light[i] = 1
            else:
                light[i] = 0
    # 3번 명령어
    elif a == 3:
        for i in range(b - 1, c):
            light[i] = 0
    # 4번 명령어
    elif a == 4:
        for i in range(b - 1, c):
            light[i] = 1
print(*light)