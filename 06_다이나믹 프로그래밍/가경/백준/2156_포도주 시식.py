import sys
input = sys.stdin.readline

n = int(input())
wines = []
for i in range(n):
    wines.append(int(input()))

if n == 1:
    print(wines[0])
elif n == 2:
    print(wines[0] + wines[1])
else:
    d = [0] * n
    d[0] = wines[0]
    d[1] = wines[0] + wines[1]
    d[2] = max(wines[0] + wines[2], wines[1] + wines[2], d[1])
    for i in range(3, n):
        # 전 포도주를 마시지 않고 현재 포도주를 마신 경우 / 전 포도주와 현재 포도주를 마신 경우 / 현재 포도주를 마시지 않는 경우
        d[i] = max(d[i - 2] + wines[i], d[i - 3] + wines[i - 1] + wines[i], d[i - 1])
    print(d[n - 1])
