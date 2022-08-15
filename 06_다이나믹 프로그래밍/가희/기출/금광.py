# n*m 크기의 금광이 있을 때, 얻을 수 있는 금의 최대 크기 구하는 프로그램

# 1*1 칸에 특정한 크기의 금이 있고(1 <= 각 위치의 금의 개수 <= 100),
# 첫 번째 열의 어느 행에서든 출발 가능
# m번에 걸쳐 오른쪽 위, 오른쪽, 오른쪽 아래로 이동 가능


# 1. 왼쪽 위에서 오는 경우(=오른쪽 아래로 이동) ~ dp[i-1][j-1]
# 2. 왼쪽 아래에서 오는 경우(=오른쪽 위로 이동) ~ dp[i+1][j-1]
# 3. 왼쪽에서 오는 경우(오른쪽으로 이동) ~ dp[i][j-1]
# 점화식) dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i+1][j-1], dp[i][j-1])

# 테스트 케이스 개수 t (1 <= t <= 1,000)
t = int(input())

for _ in range(t):
    # 금광 정보 (1 <= n,m <= 20)
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1, m): # 열
        for i in range(n): # 행
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)