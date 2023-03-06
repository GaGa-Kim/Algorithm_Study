# 9655번
# 탁자 위에 돌 n개가 있고, 두 명이서 번갈아가면서 돌을 1개 또는 3개씩
# 가져갈 때, 마지막 돌을 가져가는 사람이 이기게 된다.
# 상근이가 먼저 시작한다고 했을 때, 이기는 사람을 구하는 프로그램

# 1 ≤ N ≤ 1000
n = int(input())

if n % 2 != 0:
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
    dp[i] = min(dp[i-1], dp[i-3])+1

if dp[i] % 2 == 0:
    print('CY')
else:
    print('SK')