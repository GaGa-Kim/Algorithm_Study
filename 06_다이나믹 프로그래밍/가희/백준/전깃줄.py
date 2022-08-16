# 2565번
# 전깃줄의 개수와 연결 위치 번호가 주어질 때, 남아있는 모든 전깃줄이
# 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수 구하는 프로그램

# 1. A전봇대 기준으로 오름차순 정렬하고
# 2. B전봇대에서 최장 증가 부분 수열 구함

# 두 전봇대 사이 전깃줄 개수 (1 <= n <= 100)
n = int(input())

dp = [1] * n

# 전깃줄이 A 전봇대, B 전봇대와 연결되는 위치 번호
# 1 <= 위치 번호 <= 500, 같은 위치 두 개 이상 연결 x
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a,b))

array = sorted(array)

for i in range(n):
    for j in range(i):
        if array[j][1] < array[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
        
print(n - max(dp))