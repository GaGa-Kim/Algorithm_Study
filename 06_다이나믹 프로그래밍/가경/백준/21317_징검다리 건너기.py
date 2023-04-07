import sys
input = sys.stdin.readline

n = int(input())
stone = []
d = [1e9] * n
d[0] = 0
for i in range(n - 1):
    small, big = map(int, input().split())
    stone.append((small, big))
    # 작은 점프와 큰 점프만을 이용해 갱신
    if i + 1 < n:
        d[i + 1] = min(d[i + 1], d[i] + small)
    if i + 2 < n:
        d[i + 2] = min(d[i + 2], d[i] + big)

# 매우 큰 점프 적용해보면서 최솟값 갱신
k = int(input())
answer = d[-1]
for i in range(3, n):
    large, d1, d2 = d[i - 3] + k, 1e9, 1e9
    for j in range(i, n - 1):
        if i + 1 < n:
            d1 = min(d1, large + stone[j][0])
        if i + 2 < n:
            d2 = min(d2, large + stone[j][1])
        large, d1, d2 = d1, d2, 1e9
    answer = min(answer, large)

print(answer)