# <접두사 합을 이용하여 구간 합 빠르게 계산하기>
# 1. n개의 수에 대하여 접두사 합을 계산하여 배열 P에 저장
# 2. 매 m개의 쿼리 정보 [L, R]을 확인할 때, 구간 합은 P[R] - P[L-1]이다.

n = 5                       # 데이터 개수
data = [10, 20, 30, 40, 50] # 전체 데이터

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산
left = 3
right = 4
print(prefix_sum[4] - prefix_sum[left-1])