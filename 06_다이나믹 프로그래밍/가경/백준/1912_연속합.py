import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))

d = [-1001] * (n + 1)
for i in range(1, n + 1):
    # 현재 값 / 이전(연속된) 값에 현재 값을 더한 값 비교
    d[i] = max(array[i], d[i - 1] + array[i])
print(max(d))
