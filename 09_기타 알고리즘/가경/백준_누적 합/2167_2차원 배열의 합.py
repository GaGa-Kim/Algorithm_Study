import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 누적합 dp 테이블
d = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # d[2][2] = array[1][1] + d[2][1] + d[1][2] - d[1][1]
        # 현재 위치 값 + 이전 dp 테이블 값 - 겹치는 부분의 값
        d[i][j] = array[i - 1][j - 1] + d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1]

k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    # (x, y)의 dp 테이블 값 - (i, j)의 dp 테이블 값 + 겹치는 부분의 값
    print(d[x][y] - d[i - 1][y] - d[x][j - 1] + d[i - 1][j - 1])