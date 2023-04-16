import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
# 가치의 합이 0 ~ K원일 때의 최소 동전 갯수 DP 테이블 
d = [10001] * (k + 1)
d[0] = 0

for i in coin:
    for j in range(i, k + 1):
        # 최소 동전 갯수 갱신
        d[j] = min(d[j], d[j - i] + 1)
if d[k] == 10001:
    print(-1)
else:
    print(d[k])