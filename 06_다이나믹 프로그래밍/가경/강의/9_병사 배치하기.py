# 9_병사 배치하기.py
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n): # 두 번째 원소부터 마지막 원소까지 각 원소를 확인하며 해당 원소를 마지막 원소로 설정하는 LIS의 최대 길이를 구함
    for j in range(0, i):
        if array[j] < array[i]: # 앞에 있는 모든 원소 중에서 자기보다 해당 원소가 더 작은 경우 테이블 갱신
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))