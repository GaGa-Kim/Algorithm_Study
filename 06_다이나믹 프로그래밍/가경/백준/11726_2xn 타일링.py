import sys
input = sys.stdin.readline

d = [0] * 1001
d[1] = 1
d[2] = 2
for i in range(3, 1001):
    d[i] = d[i - 2] + d[i - 1]

n = int(input())
print(d[n] % 10007)
