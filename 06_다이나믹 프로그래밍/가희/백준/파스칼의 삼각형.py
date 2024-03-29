# 16395번
# 정수 n, k가 주어졌을 때, 
# 파스칼의 삼각형에 있는 n번째 행에서 k번째 수를 출력하는 프로그램
# 이때, 이 수는 이항계수 C(n-1, k-1)이다.

# 1. n번째 행에는 n개의 수가 있다.
# 2. 첫 번째 행은 1이다.
# 3. 두 번째 행부터, 각 행의 양 끝의 값은 1이고, 나머지 수의 값은
#   바로 위 행의 인접한 두 수의 합이다.

# 1 ≤ k ≤ n ≤ 30
n, k = map(int, input().split())

dp = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n-1][k-1])      

# 1
# 1 1
# 1 2 1
# 1 3 3 1