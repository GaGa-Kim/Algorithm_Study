import sys
input = sys.stdin.readline

n = int(input())
number = [list(map(int, input().strip())) for _ in range(n)]

answer = 1
for i in range(1, len(number[0]) + 1):
    nnmuber = []
    for j in range(n):
        if number[j][-i:] in nnmuber:
            break
        else:
            nnmuber.append(number[j][-i:])
    if len(nnmuber) == n:
        print(i)
        break