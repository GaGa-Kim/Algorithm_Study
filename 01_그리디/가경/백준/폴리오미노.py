board = input()

board = board.replace("XXXX", "AAAA") # XXXX일 경우, AAAA로 덮음
board = board.replace("XX", "BB") # XX일 경우, BB로 덮ㅇㅁ

if 'X' in board: # X일 경우, 덮을 수 없으므로 -1 출력 
    print(-1)
else:
    print(board)