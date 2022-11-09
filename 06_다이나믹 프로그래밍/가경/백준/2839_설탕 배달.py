import sys
input = sys.stdin.readline

n = int(input())
# 봉지의 갯수 DP 테이블
d = [5001] * 5001
d[3] = 1 # 3 킬로그램 설탕은 봉지 1개 필요
d[5] = 1 # 5 킬로그램 설탕은 봉지 1개 필요

for i in range(6, n + 1):
    # 이전 봉지 갯수 + 1개의 봉지
    d[i] = min(d[i - 3], d[i - 5]) + 1

print(d[n] if d[n] < 5001 else -1)