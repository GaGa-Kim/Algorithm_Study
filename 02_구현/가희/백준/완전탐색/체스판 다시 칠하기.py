# 1018번
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램

# 검,흰색이 번갈아 칠해져 있는 m x n 크기의 보드를  
# 8 x 8 크기로 잘라 다시 칠한 뒤 체스판으로 만들 것

# 8 <= n, m <= 50
n, m = map(int, input().split())

# 보드 상태 (B: 검, W: 흰)
board = []
for _ in range(n):
    board.append(input())
result = []

# i, j는 체스판(8 x 8) 검사 시작점이므로 
# 적어도 n-7, m-7 시점부터는 시작해야 함 
for i in range(n-7):
    for j in range(m-7):
        cnt_b = 0 # 맨 위쪽 위칸이 검은색인 경우
        cnt_w = 0 # 맨 위쪽 위칸이 흰색인 경우
        for a in range(i, i+8):
            for b in range(j, j+8):
                # a+b 합이 짝수이면 시작점의 색과 같아야 함
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W':
                        cnt_w += 1
                    if board[a][b] != 'B':
                        cnt_b += 1
                else: # a+b 합이 홀수이면 시작점의 색과 달라야 함
                    if board[a][b] != 'B':
                        cnt_w += 1
                    if board[a][b] != 'W':
                        cnt_b += 1
        result.append(cnt_b)
        result.append(cnt_w)
                        
print(min(result))                    

