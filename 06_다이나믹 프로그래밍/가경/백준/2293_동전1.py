import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
# 가치의 합이 0 ~ K원일 때의 동전 구성 갯수 DP 테이블 
d = [0] * (k + 1)
d[0] = 1

for i in coin:
    for j in range(i, k + 1):
        d[j] += d[j - i]
print(d[k])