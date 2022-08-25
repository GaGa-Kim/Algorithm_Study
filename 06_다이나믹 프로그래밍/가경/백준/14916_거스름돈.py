import sys
n = int(sys.stdin.readline())

# 0원, 1원, 2원, 3원, 4원, 5원, 6원, 7원, 8원, 9원
d = [-1, -1, 1, -1, 2, 1, 3, 2, 4, 3]
for i in range(10, n + 1):
    d.append(d[i - 5] + 1)

print(d[n])
