# 백준 1932번
# 맨 위층부터 시작해서 아래에 있는 수 중 하나를 선택하여
# 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가
# 되는 경로를 구하는 프로그램

# 아래층에 있는 수는 현재 층에서 선택된 수의 
# 대각선 왼쪽 또는 대각선 오른쪽만 가능
# 삼각형을 이루고 있는 각 수는 0 이상 9999 이하 정수

#--------------------책 풀이-----------------------
# 삼각형 크기 n (1 <= n <= 500)
n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

dp = []

# 두 번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i+1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        # 최대 합 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1]))


#----------------------------------------------
# 1. 맨 왼쪽과 오른쪽 열들은 자신 바로 위의 숫자 더함
# 2. 그외 ~ 왼쪽 위와 오른쪽 위 비교해서 큰 값 더함

# 삼각형 크기 n (1 <= n <= 500)
n = int(input())

dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 맨 왼쪽 열이면
            dp[i][j] += dp[i-1][j]
        elif j == i : # 맨 오른쪽 열이면
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))