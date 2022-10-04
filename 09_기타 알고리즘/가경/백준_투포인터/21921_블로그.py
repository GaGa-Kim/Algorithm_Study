import sys
input = sys.stdin.readline

n, x = map(int, input().split())
people = list(map(int, input().split()))

# 접두사 합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in people:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
result = []
count = 0  
while count + x <= n:
    result.append(prefix_sum[count + x] - prefix_sum[count])
    count += 1

# 구간 합 중에서 가장 큰 방문자 수
if max(result) == 0:
    print("SAD")
else:
    print(max(result))
    print(result.count(max(result)))