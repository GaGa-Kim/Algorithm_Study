n = int(input())
m = input()
row = column = 0

# 목판의 수직, 수평을 지나갔는지 표시
vertical = [[False] * 10 for _ in range(10)]
horizontal = [[False] * 10 for _ in range(10)]

# 격자 바깥으로 나갔는지 아닌지 체크
def check(row, column):
    if (row < 0 or row >= n or column < 0 or column >= n): 
        return False
    return True

for i in range(len(m)):
    if m[i] == 'U':
        if check(row - 1, column):
            vertical[row][column] = True
            vertical[row - 1][column] = True
            row = row - 1
    elif m[i] == 'D':
        if check(row + 1, column):
            vertical[row][column] = True
            vertical[row + 1][column] = True
            row = row + 1
    elif m[i] == 'L':
        if check(row, column - 1):
            horizontal[row][column] = True
            horizontal[row][column - 1] = True
            column = column - 1
    elif m[i] == 'R':
        if check(row, column + 1):
            horizontal[row][column] = True
            horizontal[row][column + 1] = True
            column = column + 1

# 그리기
for i in range(n):
    for j in range(n):
        if (vertical[i][j] and horizontal[i][j]):
            print('+', end="")
        else:
            if vertical[i][j]:
                print('|', end="")
            elif horizontal[i][j]:
                print('-', end="")
            else:
                print('.', end="")
    print()