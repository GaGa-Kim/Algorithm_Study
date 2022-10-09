import sys, copy
input = sys.stdin.readline

r, c = map(int, input().split())
map = [list(input().rstrip()) for _ in range(r)]
result = copy.deepcopy(map)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for y in range(r):
    for x in range(c):
        count = 0
        if map[y][x] == '.':
            continue
        # 섬이면서 인접한 4칸에 바다가 있는지 확인
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                if map[ny][nx] == '.':
                    count += 1
            else: # 범위를 벗어나는 칸은 모두 바다
                count += 1
        # 인접한 3칸 이상이 바다이면 섬이 바다로 바뀜
        if count >= 3:
            result[y][x] = '.'

# 섬이 존재하는 첫 번째 열과 마지막 열
start_y, end_y = 0, 0
for i in range(r):
    if 'X' in result[i]:
        start_y = i
        break
for i in range(r - 1, -1, -1):
    if 'X' in result[i]:
        end_y = i
        break

# 섬이 존재하는 행
x = []
for j in range(c):
    for i in range(start_y, end_y + 1):
        if 'X' == result[i][j]:
            x.append(j)
            break

for y in range(start_y, end_y + 1):
    print("".join(result[y][x[0]:x[-1] + 1]))