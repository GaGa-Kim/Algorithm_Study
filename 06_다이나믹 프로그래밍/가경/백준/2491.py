import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
d1 = [1] * n # 연속해서 커지는 경우 DP 테이블
d2 = [1] * n # 연속해서 작아지는 경우 DP 테이블

for i in range(1, n):
    # 연속해서 커지는 경우
    if array[i] >= array[i - 1]:
        d1[i] = max(d1[i], d1[i - 1] + 1)
    # 연속해서 작아지는 경우
    if array[i] <= array[i - 1]:
        d2[i] = max(d2[i], d2[i - 1] + 1)
print(max(max(d1), max(d2)))