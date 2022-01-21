# <--시뮬레이션 유형-->
# 연산 횟수는 이동 횟수에 비례 
# 이동 횟수 = N ~> 시간복잡도 O(N)

# A는 N*N 크기의 정사각형 공간 위에 있음, 이 공간은 1*1 정사각형으로 나뉘어져 있음
# 가장 왼쪽 위 (1,1), 가장 오른쪽 아래 (N,N)
# A는 L, R, U, D 방향(좌, 우 , 상, 하)으로 한 칸씩이동 가능 => 계획서로 주어짐
# 시작 좌표는 (1,1)
# N*N 벗어나면 무시
# 여행 계획서가 주어졌을 때, A가 최종으로 도착할 지점 좌표 출력하는 프로그램

# N*N 크기 공간, 1 <= N <= 100
n = int(input())
x, y = 1, 1 # 초기 위치

# 계획서, 1 <= 이동횟수 <= 100
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1] # 행
dy = [-1, 1, 0, 0 ] # 열
move_type = ['L', 'R', 'U', 'D']

# 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # N*N 공간 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny 

print(x, y)


