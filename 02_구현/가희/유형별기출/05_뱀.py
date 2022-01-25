# 백준 3190 번
# 시뮬레이션 유형

# N*N 정사각 보드, 보드 상하좌우 끝에 벽 존재
# 뱀 초기 위치) 맨 위 맨 좌측
# 뱀 초기 길이) 1, 
# 뱀 초기 방향) 오른쪽 

# <규칙> 뱀은 매 초마다 이동
# ㉠ 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킴
# ㉡ 이동한 칸에 사과 o ~ 사과 없어지고 꼬리 움직이지 x
# ㉢ 이동한 칸에 사과 x ~ 몸 길이 줄이고 꼬리 위치한 칸 비워줌(총 몸길이 변화x)
# ㉣ 벽 또는 몸통에 부딪히면 게임 종료 
#    => 매 시점마다 뱀 존재 위치 항상 2차원 리스트에 기록해야 함

# 게임이 몇 초에 끝나는지 출력


n = int(input()) # 보드 크기 (2 <= N <= 100)
k = int(input()) # 사과 개수 (0 <= K <= 100)
data = [[0]*(n+1) for _ in range(n+1)] # 맵 정보, index 1부터 시작하기 위함
info = [] # 뱀 방향 회전 정보

# 사과 위치 맵에 1로 표시
for _ in range(k):
    a, b = map(int, input().split()) # 사과 위치 (행, 열)
    data[a][b] = 1

# 뱀의 방향 변환 횟수 1 <= L <= 100
l = int(input())
# 뱀의 방향 변환 정보, 정수 X와 문자 C로 구성
# X <= 10,000 정수
for _ in range(l):
    x, c = input().split() # X초 후 c(L/D)로 90도 회전
    info.append((int(x), c))

# 뱀 이동 방향 벡터(동->남->서->북) ~ 초기 방향이 오른쪽이므로
# 2차원 배열 상에서 이동할 때 이동 방향 벡터 정의
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]

def turn(dir, c):
    if c == 'L':
        dir = (dir-1) % 4 # %4 => 0~>3 , 3~0
    else:
        dir = (dir+1) % 4
    return dir

def simulate():
    x, y = 1, 1 # 뱀 초기 머리 위치
    data[x][y] = 2 # 뱀 존재 위치 ~> 2로 표시
    dir = 0 # 뱀 초기 방향 ~> 동쪽(오른쪽)
    
    time = 0 # 시작 뒤 지난 시간
    index = 0 # 다음에 회전할 정보 위한 인덱스
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    
    while True:
        # ㉠ 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킴
        nx = x + dx[dir] 
        ny = y + dy[dir]
        # 맵 범위 안, 뱀의 몸통이 없는 위치
        if nx>=1 and nx<=n and ny>=1 and ny<=n and data[nx][ny]!=2:
            # ㉢ 사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0 
            
            # ㉡ 사과가 있다면 이동 후 꼬리 그대로
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        
        # 벽이나 몸통과 충돌한 경우
        else:
            time += 1
            break
    
        x, y = nx, ny # 다음 위치로 머리 이동
        time += 1
        # 회전할 시간인 경우 회전
        if index < l and time == info[index][0]:
            dir = turn(dir, info[index][1])
            index += 1
        
        return time

print(simulate())