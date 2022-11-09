import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 조합 DP 테이블
d = [[0 for _ in range(101)] for _ in range(101)]
for i in range(1, 101): 
    d[i][0] = 1 # iC1 = 1
    d[i][i] = 1 # 1C1 = 1
for i in range(2, 101):
    for j in range(1, i):
        # 조합의 점화식은 n-1Cr-1 + n-1Cr
        d[i][j] = d[i - 1][j - 1] + d[i - 1][j] 

print(d[n][m])