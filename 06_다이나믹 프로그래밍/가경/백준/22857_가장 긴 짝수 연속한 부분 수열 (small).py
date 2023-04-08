import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
d = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(k + 1):
        # 짝수일 때
        if s[i] % 2 == 0:
            d[i][j] = d[i - 1][j] + 1
        # 홀수일 때
        if j != 0 and s[i] % 2 != 0:
            d[i][j] = d[i - 1][j - 1]

result = []
for i in d:
    result.append(i[k])

print(max(result))