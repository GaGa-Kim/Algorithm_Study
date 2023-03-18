# 2579번
# 각 계단에 쓰여 있는 점수가 주어질 때, 얻을 수 있는 총 점수의 최댓값

# 1.계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다.
# 2.연속된 세 개의 계단을 모두 밟아서는 안 된다. (시작점은 계단x)
# 3.마지막 도착 계단은 반드시 밟아야 한다.


# 계단 개수 (<= 300)
n = int(input())

# 점수 <= 10,000
s = [int(input()) for _ in range(n)]

dp = [0] * 300
if n <= 2:
    print(sum(s))
else:
    dp[0] = s[0]
    dp[1] = s[0] + s[1]
    dp[2] = max(s[0], s[1]) + s[2]

    for i in range(3, n):
        dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

    print(dp[n-1])

"""
dp[4] = dp[1]+s[3]+s[4] or dp[2]+s[4]

dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
"""
