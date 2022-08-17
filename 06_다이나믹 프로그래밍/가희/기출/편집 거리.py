# 문자열 A를 B로 만드는 최소 편집 거리를 계산하는 프로그램

# 편집 거리) 문자열 A를 B로 만들기 위해 사용한 연산 수
# 가능한 연산: 특정 위치 삽입, 삭제, 교체

# 1. 두 문자가 같은 경우: dp[i][j] = dp[i-1][j-1]
#    ~ 왼쪽 위에 해당하는 수 그대로 삽입
# 2. 두 문자가 다른 경우: dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
#   ~ 왼쪽(삽입), 위쪽(삭제), 왼족 위(교체)에 해당하는 수 중 최솟값 + 1


def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # dp 테이블 초기 설정
    for i in range(1, n+1):
        dp[i][0] = i
    for j in range(1, m+1):
        dp[0][j] = j
    
    # 최소 편집 거리 계산
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 두 문자 같으면 왼쪽 위 해당하는 수 그대로 삽입
            if str1[i-1] == str[j-1]:
                dp[i][j] = dp[i-1][j-1]
            
            # 두 문자 다를 경우
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    
    return dp[n][m]

str1 = input()
str2 = input()

print(edit_dist(str1, str2))
