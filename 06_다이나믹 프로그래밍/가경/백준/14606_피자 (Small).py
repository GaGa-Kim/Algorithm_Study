import sys
n = int(sys.stdin.readline())

d = [0] * 11
d[1] = 0
d[2] = 1
for i in range(3, n + 1):
    # 즐거움의 최댓값을 위해 중간값으로 높이를 정함
    h = i // 2
    # 이번 피자탑 분리로 인해 즐거움 + 이전까지의 즐거움
    d[i] = h * (i - h) + d[h] + d[i - h]

print(d[n])