# 백준 18353번
# 남아 있는 병사의 수가 최대가 되도록 열외시켜야 하는 
# 병사의 수 출력하는 프로그램

# 각각 특정 값의 전투력을 보유한 n명의 병사가 무작위로 나열됨
# 전투력이 높은 순대로 내림차순으로 배치
# 특정 위치에 있는 병사를 열외 시키는 방식


# 최장 증가 부분 수열(LIS) 사용

#----------------------책 풀이----------------------
# 모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]

import sys
input = sys.stdin.readline

# 병사 수 (1 <= n <= 2,000)
n = int(input())

# 각 병사의 전투력 ( <= 10,000,000)
array = list(map(int, input().split()))
# 순서 뒤집어 최장 증가 부분 수열 문제로 변환
array.reverse() 

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소 수 출력
print(n - max(dp))

#----------------------------------------------------
# 모든 0 <= j < i 에 대해, dp[i] = max(dp[i], dp[j]+1) if array[j] > array[i]

import sys
input = sys.stdin.readline

# 병사 수 (1 <= n <= 2,000)
n = int(input())

# 각 병사의 전투력 ( <= 10,000,000)
array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        # 내림차순이면
        if array[j] > array[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 열외시켜야 하는 병사의 최소 수 출력
print(n - max(dp))