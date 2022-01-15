# 2중 반복문 구조 이용

# 행 n, 열 m 공백 구분 입력
# 1 <= n, m <= 100
import re


n, m = map(int, input().split())

result = 0 
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001 #각 숫자가 10,000 이하 자연수이므로
    for j in range(m):
        #현재 줄에서 최솟값 찾기
        min_value = min(min_value, j)
    # 최솟값들 중 최댓값
    result = max(result, min_value)
    
print(result)