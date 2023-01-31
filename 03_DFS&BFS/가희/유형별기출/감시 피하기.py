# 백준 18428번

# 파이썬 조합 라이브러리 이용 풀이
# 장애물을 정확히 설치하는 모든 경우를 확인하여, 
# 매 경우마다 모든 학생을 감시로부터 피하도록 할 수 있는지 여부 출력
from itertools import combinations

n = int(input())    # 복도 크기 n x n
board = []          # 복도 정보
teachers = []       # 모든 선생님 위치 정보
spaces = []         # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님 위치 정보 저장
        if board[i][j] == 'T':
            teachers.append((i,j))
        # 장애물을 설치할 수 있는 빈 공간 위치 정보 저장
        if board[i][j] == 'X':
            spaces.append((i,j))
            
# 특정 방향으로 감시를 진행 (학생 발견: True, 미발견: False)
def watch(x, y, dir):
    # 왼쪽 방향 감시
    if dir == 0:
        while y >= 0:
            # 학생이 있는 경우
            if board[x][y] == 'S':
                return True
            # 장애물이 있는 경우
            if board[x][y] == 'O':
                return False
            y -= 1
    # 오른쪽 방향 감시
    if dir == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽 방향 감시
    if dir == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False 
            x -= 1
    # 아래쪽 방향 감시
    if dir == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님 위치 하나씩 확인
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

# 학생이 한 명이라도 감지되지 않도록 설치할 수 있는지 여부
find = False

# 빈 공간에서 3개를 뽑는 모든 조합 확인
for data in combinations(spaces, 3):
    # 장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우 발견
        find = True
        break
    
    # 설치된 장애물 다시 없애기
    for x, y in data:
        board[x][y] = 'X'
        

if find:
    print('YES')
else:
    print('NO')
