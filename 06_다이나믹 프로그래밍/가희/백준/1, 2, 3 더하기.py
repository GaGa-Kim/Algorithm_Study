# 9095번
# 정수 n이 주어졌을 때, 
# n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = sum(dp[i-3:i])

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
    
    
"""
dp[1]=1
dp[2]=2
dp[3]=4
dp[4]=7
dp[5]=13
dp[6]=24
if i > 3
dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
"""

