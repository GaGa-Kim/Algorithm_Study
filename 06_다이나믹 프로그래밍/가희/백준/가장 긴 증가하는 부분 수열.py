# 11053번
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램


# 수열 a의 크기 (1 ≤ n ≤ 1,000)
n = int(input())

# 수열 a (1 ≤ a ≤ 1,000)
a = list(map(int, input().split()))

# a[i]를 마지막 원소로 가질 때 LIS의 길이
dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))
