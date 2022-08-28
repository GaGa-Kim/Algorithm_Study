# 2512번
# 여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때,
# 아래 조건을 모두 만족하도록 예산을 배정하는 프로그램

# 가능한 한 최대의 총 예산을 다음 방법으로 배정
# 1. 모든 요청이 배정될 수 있는 경우에는 요청 금액 그대로 배정
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여
#   그 이상인 예산 요청에는 모두 상한액 배정,
#   상한액 이하의 예산 요청에 대해서는 요청한 금액 그대로 배정

import sys
input = sys.stdin.readline

# 지방의 수 n (3 <= n <= 10,000)
n = int(input())
# 각 지방의 예산 요청 (1 <= 예산 요청 <= 100,000)
array = list(map(int, input().split()))
# 총 예산
m = int(input())

start, end = 0, max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in array:
        if i > mid:
            total += mid
        else:
            total += i
    
    if total <= m: 
        start = mid + 1
    else:
        end = mid - 1

print(end)