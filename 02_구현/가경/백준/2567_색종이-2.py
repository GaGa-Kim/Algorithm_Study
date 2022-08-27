n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1

count = 0
for i in range(1, 101):
    for j in range(1, 101):
        if array[i][j] == 1:
            tmp = 0
            for k in range(4):
                dx = [0, 0, -1, 1]
                dy = [-1, 1, 0, 0]
                nx = i + dx[k]
                ny = j + dy[k]
                if array[nx][ny] == 1:
                    tmp += 1
            # 상하좌우 중 3칸이 1이면 1
            if tmp == 3:
                count += 1
            # 상하좌우 중 2칸이 1이면 모서리이므로 2
            elif tmp == 2:
                count += 2
print(count)