import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

# 증가하는 부분 수열의 원소 합
d = array[:]
for i in range(1, n):
    for j in range(0, i):
        # 앞에 있는 모든 원소 중에서 자기보다 해당 원소가 더 작은 경우, 증가하는 부분 수열의  원소 합으로 갱신
        if array[j] < array[i]:
            d[i] = max(d[i], d[j] + array[i])
print(max(d))