import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

# 건너갈 수 있는지 여부
d = [0] * n
d[0] = 1
# i번째 돌에서 j번째 돌로 건너갈 수 있는지 확인
for i in range(n - 1):
    for j in range(i + 1, n):
        if d[i] and (j - i) * (1 + abs(a[j] - a[i])) <= k:
            d[j] = 1

if d[n - 1]:
    print("YES")
else:
    print("NO")