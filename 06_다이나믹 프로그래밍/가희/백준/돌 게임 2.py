# 9656번
# 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램

# 탁자 위에 n개의 돌이 있고, 두 사람이 턴을 번갈아가면서 돌을 가져감
# 돌은 1개 또는 3개 가져갈 수 있고, 마지막 돌을 가져가는 사람이 짐
# SK가 먼저 시작

# 1 ≤ N ≤ 1000
n = int(input())

if n % 2 == 0:
    print('SK')
else:
    print('CY')

# dp 풀이--------------------------
# 1 ≤ N ≤ 1000
n = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4, n+1):
    dp[i] = min(dp[i-1], dp[i-3]) + 1

if dp[n] % 2 == 0:
    print('SK')
else:
    print('CY')