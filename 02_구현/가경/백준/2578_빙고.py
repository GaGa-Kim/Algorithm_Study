# 빙고판
board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

# 사회자가 부르는 수는 한 줄 리스트로 입력
num = list(map(int, input().split()))
for _ in range(4):
    num += list(map(int, input().split())) 

# 각 5번 불려야 한 줄 완성
check = [0] * 12 # 행 5개 + 열 5개 + 대각선 2개
# 완성된 선 갯수
line = 0 
# 빙고 여부
bingo = False
for i in range(25): # 사회자가 25번 부를 동안
    if bingo == True:
        break
    for j in range(5):
        if bingo == True:
            break
        for k in range(5):
            if bingo == True:
                break
            if num[i] == board[j][k]:
                board[j][k] = 0
                check[j] += 1 # 행 (ㅡ)
                check[k + 5] += 1 # 열 (|)
                if j == k:
                    check[10] += 1 # 대각선 (\)
                if j + k == 4:
                    check[11] += 1 # 반대 대각선 (/)
                for l in range(12):
                    if check[l] == 5:
                        check[l] = 0
                        line += 1 # 한 줄 완성
                        if line == 3: # 세 줄 완성일 경우 빙고
                            bingo = True
                            break
print(i)