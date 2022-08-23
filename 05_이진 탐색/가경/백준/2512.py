import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start, end = 0, max(budget)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        # 이상일 경우 상한액 배정
        if budget[i] >= mid:
            total += mid
        else:
            total += budget[i]     
    if total <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)