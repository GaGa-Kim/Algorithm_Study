# 2217번
# n개의 로프에 대한 정보가 주어졌을 때, 들어올릴 수 있는 물체의 최대 중량 구하는 프로그램
# (모든 로프를 사용할 필요는 없다.)
# k개의 로프를 사용하여 중량인 w인 물체를 들어올릴 때,
# 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

# 최종 무게 = 가장 가벼운 무게를 들 수 있는 로프의 최대 중량 * 연결 로프 개수

import sys
input = sys.stdin.readline

# 1 <= n <= 100,000
n = int(input())
# 각 로프가 버틸 수 있는 최대 중량(<= 10,000)
data = [int(input()) for i in range(n)]
data.sort(reverse=True)

result = 0
for i in range(n):
    result = max(result, data[i] * (i+1))
    
print(result)

