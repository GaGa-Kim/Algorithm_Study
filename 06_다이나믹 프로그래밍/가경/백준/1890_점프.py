import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0 for _ in range(n)] for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        # 가장 오른쪽 아래 칸이라면
        if i == n - 1 and j == n - 1:
            print(d)
            print(d[i][j])
            break
        # 현재 칸에서 갈 수 있는 거리
        dist = board[i][j]
        # 오른쪽으로 이동
        if j + dist < n:
            d[i][j + dist] += d[i][j]
        # 아래쪽으로 이동
        if i + dist < n:
            d[i + dist][j] += d[i][j]
