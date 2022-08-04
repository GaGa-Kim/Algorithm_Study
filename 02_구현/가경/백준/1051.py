import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

answer = 1
for i in range(n):
    for j in range(m):
        # 정사각형 한 변의 길이의 최대 크기는 n과 m 중의 최솟값
        for k in range(min(n, m)):
            if n <= i + k or m <= j + k:
                break
            if (board[i][j] == board[i][j + k] == board[i + k][j] == board[i + k][j + k]):
                answer = max(answer, k + 1)
print(answer**2)