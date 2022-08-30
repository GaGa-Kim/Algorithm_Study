# 2805번
# 적어도 m미터의 나무를 집에 가져가기 위해 
# 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

import sys
input = sys.stdin.readline

# 나무의 수 n, 집으로 가져갈 나무 길이 m
# (1 <= n <= 1,000,000 / 1 <= m <= 2,000,000,000)
n, m = map(int, input().split())

# 나무 높이 (0 <= 높이 <= 1,000,000,000)
array = list(map(int, input().split()))

start, end = 1, max(array)

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for i in array:
        if i > mid:
            total += i-mid
            
        if total > m: # 절단한 나무가 이미 m 초과하면 종료
            break
    
    if total >= m:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)