import sys
n = int(sys.stdin.readline())

d = [0] * 81
d[1] = 1
d[2] = 1

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print((d[n] + d[n - 1]) * 2 + d[n] * 2)
# 또는 d[n] * 2 + d[n - 1] * 2