# 2775번
# a층 b호에 살려면 a-1층의 1호부터 b호까지 사람들의 수의 합만큼
# 사람을 데려와 살아야 할 때, 양의 정수 k와 n에 대해 k층 n호에는
# 몇 명이 살고 있는지 출력하는 프로그램
# (단, 0층부터 있으며, 각층은 1호부터 시작한다. 
# 0층의 i호에는 i명이 산다.)

t = int(input())
for _ in range(t):
    # 1 ≤ k, n ≤ 14
    k = int(input()) 
    n = int(input()) 
    
    dp = [[0] * (n+1) for _ in range(k+1)]
    
    for i in range(1, n+1):
        dp[0][i] = i
        
    for i in range(1, k+1): 
        for j in range(1, n+1):
            dp[i][j] = sum(dp[i-1][:j+1])
    
    print(dp[k][n])
    
    
# 2트 때 코드 개선하기
