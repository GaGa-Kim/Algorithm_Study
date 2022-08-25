x, y = map(int, input().split())
x_list = [0, x]
y_list = [0, y]

for _ in range(int(input())):
    xy, length = map(int, input().split())
    if xy == 0: # 가로
        y_list.append(length)
    else: # 세로
        x_list.append(length)

x_list.sort()
y_list.sort()

answer = 0
for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        width = x_list[i] - x_list[i - 1]
        height = y_list[j] - y_list[j - 1]
        answer = max(answer, width * height)

print(answer) 