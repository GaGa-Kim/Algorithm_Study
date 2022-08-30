# 1654번
# 길이가 제각각인 k개의 랜선으로 같은 길이의 n개의 랜선을
# 만들 때, 만들 수 있는 최대 랜선의 길이 구하는 프로그램
# (n개 보다 많이 만드는 것도 n개를 만드는 것에 포함됨)

import sys 
input = sys.stdin.readline

# 1 <= k <= 10,000
# 1 <= n <= 1,000,000 (k <= n)
k, n = map(int, input().split())

# k개의 랜선의 길이 (랜선 <= 2^31 - 1)
array = [int(input()) for _ in range(k)]

start, end = 1, max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2 
    
    for i in array:
        total += i // mid
        
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)