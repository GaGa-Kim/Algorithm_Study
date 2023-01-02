# 14503번 (04-04 게임 개발과 유사)
# 로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램

# 지도는 n x m으로 1 x 1 크기 정사각형으로 구성
# 지도의 각 칸은 (r,c)으로 표현 ~ 북쪽으로부터 r만큼, 서쪽으로 c만큼 떨어진 칸의 개수

# 1. 현재 위치 청소
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색
#   2-1) 왼쪽에 청소 안 한 공간 있으면 좌회전 뒤 한 칸 전진하고 1번
#   2-2) 왼쪽 청소 공간 없으면, 좌회전 후 2번
#   2-3) 네 방향 모두 청소 o 또는 벽이면, 방향 유지 + 한 칸 후진 후 2번
#   2-4) 네 방향 모두 청소 o 또는 벽, 그리고 뒤가 벽이라 후진 못하면 작동 멈춤

# 시간 초과 ----------------------------------------------------
import sys 
input = sys.stdin.readline

# 세로 n, 가로 m (3 <= n, m <= 50)
n, m = map(int, input().split())

# 방문 위치 
visited = [[0] * m for _ in range(n)]

# 청소기가 있는 좌표 (r,c)와 방향 d
# d ~ 0: 북, 1: 동, 2: 남, 3: 서 (시계)
r, c, d = map(int, input().split())
visited[r][c] = 1   # 청소기 현재 위치 표시

# 지도 (0: 빈 칸, 1: 벽)
board = [list(map(int, input().split())) for _ in range(n)]

# 이동 방향 (북동남서)
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

# 좌회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
turn_time = 0
while True:
    # 현재 위치에서 현재 방향을 기준으로 왼쪽부터 차례대로 탐색
    turn_left()
    nr = r + dr[d]
    nc = c + dc[d]
    
    # 왼쪽에 청소 안 한 공간 o ~ 좌회전 + 한 칸 전진(청소)하고 청소
    if visited[nr][nc] == 0 and board[nr][nc] == 0:
        r, c = nr, nc
        cnt += 1
        turn_time = 0
        continue
    # 왼쪽에 청소할 공간 없으면, 좌회전만 함
    else:
        turn_time += 1
    
    # 네 방향 모두 청소 되어 있으면 
    if turn_time == 4:
        # 방향 유지 + 한 칸 후진 
        nr = r - dr[d]
        nc = c - dc[d]
        if board[nr][nc] != 1: # 뒤가 벽이 아닐 때만 후진 가능
            r, c = nr, nc
        else: # 뒤가 벽이면 후진 안 하고 작동 멈춤
            break
        turn_time = 0
        

# 로봇 청소기가 청소하는 칸 개수 출력
print(cnt)


# 40ms ----------------------------------------------------
n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)]
r, c, d = map(int, input().split())
visited[r][c] = 1

board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
while True:
    flag = 0
    
    for _ in range(4):
        nr = r + dr[(d+3) % 4]
        nc = c + dc[(d+3) % 4]
        d = (d+3) % 4
        
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                cnt += 1
                r = nr
                c = nc
                flag = 1
                break
    if flag == 0:
        if board[r - dr[d]][c - dc[d]] == 1:
            print(cnt)
            break
        else:
            r, c = r - dr[d], c - dc[d]