# 1010번
# 다리를 서쪽 사이트 개수(n)만큼 지으려고 할 때, 다리를 지을 수 있는 경우의 수 구하는 프로그램
# 서쪽에는 n개의 사이트, 동쪽에는 m개의 사이트가 있고(n <= m), 이 두 사이트를 다리로 연결하려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다.


# 1. 서 = 1, 동 = n     -> 다리 n개
# 2. 서 = 동            -> 다리 1개
# 3. 서 = n, 동 = m     -> (서 n, 동 m-1) + (서 n-1, 동 m-1)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 0 < n ≤ m < 30
    n, m = map(int, input().split())
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1:
                dp[i][j] = j
                continue
            if i == j:
                dp[i][j] = 1
            else:
                if i < j:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])
    
# 팩토리얼+조합 코드 추가하기
