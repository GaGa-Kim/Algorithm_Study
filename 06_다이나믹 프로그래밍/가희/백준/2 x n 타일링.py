# 11726번
# 2 x n 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하는 프로그램


# 1 ≤ n ≤ 1,000
n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])


"""
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
...
dp[i] = dp[i-1] + dp[i-2]
"""