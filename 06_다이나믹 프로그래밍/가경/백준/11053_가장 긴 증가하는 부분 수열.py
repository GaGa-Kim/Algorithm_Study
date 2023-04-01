import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# array[i]를 마지막 값으로 가지는 가장 긴 증가하는 부분 수열의 길이
d = [1] * n
# 두 번째 원소부터 마지막 원소까지 각 원소를 확인하며 해당 원소를 마지막 원소로 설정하는 LIS의 최대 길이를 구함
for i in range(1, n):
    for j in range(0, i):
        # 앞에 있는 모든 원소 중에서 자기보다 해당 원소가 더 작은 경우 테이블 갱신
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))