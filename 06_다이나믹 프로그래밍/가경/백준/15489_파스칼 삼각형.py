import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())

# 파스칼 삼각형 다이나믹 프로그래밍
d = [[1], [1, 1]]
for i in range(2, r + w - 1):
    row = [1]
    for j in range(1, i):
        row.append(d[i - 1][j - 1] + d[i - 1][j])
    row.append(1)
    d.append(row)

answer = 0
h = 1
for i in range(r - 1, r + w - 1):
    for j in range(h):
        answer += d[i][c - 1 + j]
    h += 1
print(answer)
