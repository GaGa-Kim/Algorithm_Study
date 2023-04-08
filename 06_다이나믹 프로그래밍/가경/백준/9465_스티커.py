import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]
    for i in range(1, n):
        if i == 1:
            # 대각선에 있는 값을 가질 수 있음
            d[0][1] += d[1][0]
            d[1][1] += d[0][0]
        else:
            # 전 열의 대각선 또는 전전 열의 대각선 둘 중 큰 값을 자신에 더함
            d[0][i] += max(d[1][i - 1], d[1][i - 2])
            d[1][i] += max(d[0][i - 1], d[0][i - 2])
    print(max(d[0][n - 1], d[1][n - 1]))
