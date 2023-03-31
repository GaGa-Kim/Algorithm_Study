import sys
input = sys.stdin.readline

n = int(input())
stairs = [0 for _ in range(301)]
for i in range(n):
    stairs[i] = int(input())

d = [0] * 301
d[0] = stairs[0]
d[1] = stairs[0] + stairs[1]
# 한 계단 + 다음 계단 / 다음 다음 계단
d[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
for i in range(3, n):
    # 마지막 단계의 전 계단을 밟은 경우 / 전 단계를 밟지 않은 경우
    d[i] = max(d[i - 3] + stairs[i - 1] + stairs[i], d[i - 2] + stairs[i])
print(d[n - 1])
