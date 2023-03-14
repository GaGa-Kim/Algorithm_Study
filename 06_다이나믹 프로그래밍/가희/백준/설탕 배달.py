# 2839번
# 설탕을 정확히 n kg 배달해야 할 때, 가져가야 하는 봉지의 최소 개수를 구하는 프로그램
# 봉지는 3, 5kg가 있음


# 3 ≤ n ≤ 5000
n = int(input())

# 각 무게별 사용하는 봉지의 최솟값
# n+5 ~ n의 값이 5보다 작은 경우 IndexOutOfRange오류 방지
dp = [5001] * (n+5) 

dp[3] = 1
dp[5] = 1

for i in range(6, n+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

print(dp[n] if dp[n] < 5001 else -1)