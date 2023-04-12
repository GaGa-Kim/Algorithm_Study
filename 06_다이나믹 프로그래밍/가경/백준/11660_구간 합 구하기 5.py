import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tables = []
for _ in range(n):
    table = list(map(int, input().split()))
    tables.append(table)

# 누적합을 가지는 DP 테이블
d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 현재 자리 + 누적합
        d[i][j] = d[i][j - 1] + d[i - 1][j] - d[i - 1][j - 1] + tables[i - 1][j - 1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # (x2, y2)까지의 누적합 - (0, 0)부터 (x1, y1) 전까지의 누적합 
    answer = d[x2][y2] - d[x2][y1 - 1] - d[x1 - 1][y2] + d[x1 - 1][y1 - 1]
    print(answer)

