import sys
input = sys.stdin.readline

n = int(input())
mine = [list(input()) for _ in range(n)] # 지뢰의 위치
board = [list(input()) for _ in range(n)] # 플레이된 게임의 정보
result = [['.'] * n for _ in range(n)]

# 인접한 8개의 칸 방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for x in range(n):
    for y in range(n):
        # 지뢰가 없으면서 열린 칸
        if mine[x][y] == '.' and board[x][y] == 'x':
            count = 0 # 주변 지뢰 수
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                # 공간을 벗어나면 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if mine[nx][ny] == '*':
                    count += 1
            result[x][y] = count
        # 지뢰가 있으면서 열린 칸
        if mine[x][y] == '*' and board[x][y] == 'x':
            for i in range(n):
                for j in range(n):
                    # 지뢰가 있는 칸을 모두 표시함
                    if mine[i][j] == '*':
                        result[i][j] = '*'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()