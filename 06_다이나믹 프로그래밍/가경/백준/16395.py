import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 파스칼의 삼각형의 첫 번째 행과 두 번째 행
d = [[1], [1, 1]]
# 파스칼의 삼각형의 세 번째 행부터 n번째 행
for i in range(2, n):
    # 1, 바로 위 행의 인접한 두 수의 합, 1
    row = [1]
    for j in range(1, i):
        row.append(d[i - 1][j - 1] + d[i - 1][j])
    row.append(1)
    d.append(row)
print(d[n - 1][k - 1])