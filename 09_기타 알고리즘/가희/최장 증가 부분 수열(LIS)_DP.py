# 일반적으로 최장 증가 부분 수열의 길이를 구하는 
# 간편한 방법은 DP를 이용하는 것

n = 8 # 원소 개수
arr = {6, 2, 5, 1, 7, 4, 8, 3}
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]: 
            dp[i] = max(dp[j]+1, dp[i])
            
# (1) j번째 인덱스에서 끝나는 최장 증가 부분 수열의 마지막에
#    arr[i]를 추가했을 때의 LIS 길이와 
# (2) 추가하지 않고 기존의 dp[i] 값을 비교하여
# 더 큰 값으로 dp[i] 갱신

# 시간 복잡도는 O(n^2)
# LIS의 길이를 구하기 위해 이분탐색을 이용하면 개선 가능