# 시뮬레이션 유형(백준 14503번와 유사)

# 세로*가로 = N * M (3 <= N, M <=50)
n, m = map(int ,input().split())

# 방문 위치 저장 위한 맵 생성, 0으로 초기화
d = [[0]*m for _ in range(n)]

# 게임 캐릭터가 있는 칸의 좌표 (x,y)와 
# 바라보는 방향 direction
x, y, dir = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보 
# 북쪽~남쪽 순서대로, 서쪽~동쪽 순서대로
# 맵 외곽은 항상 바다로 되어있음(육지:0, 바다:1)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 벡터 정의
# 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 좌회전
def turn_left():
    # 함수 밖에서 선언된 전역 변수이기 때문에 global
    global dir
    dir -= 1
    if dir == -1:
        dir = 3
        
# 시뮬 시작
count = 1
turn_time = 0
while True:
    # 1. 현재 위치에서 현재 방향을 기준으로 
    # 왼쪽 방향(반시계 방향 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
    turn_left()
    nx = x + dx[dir] 
    ny = y + dy[dir]
    
    # 2-1. 아직 가보지 않은 칸 O, 육지인 경우 ~> 좌회전 후 1칸 전진
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue # 밑 코드는 건너뛰고 다시 반복문 처음으로 
    
    # 2-2. 왼쪽 방향에 안 가본 칸 x ~> 좌회전만 하고 1단계로 돌아감
    else:
        turn_time += 1
    
    # 3. 네 방향 모두 가봄 or 바다 ~> 방향 유지한 채로 1칸 후진, 1단계로 돌아감
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 이동할 수 있을 때 이동
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다이면 움직임 종료
        else:
            break
        
        turn_time = 0
        
        
print(count)


# 방향을 설정해서 이동하는 문제에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적
# 파이썬에서 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적