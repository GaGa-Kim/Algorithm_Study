data = []
answer = "Valid"
visited = []

for _ in range(36):
    data.append(input())

for i in range(35):
    # 모든 경로에서 가로, 세로 2, 1 이동 또는 1, 2 이동을 했는지와 이미 방문한 곳이 아닌지 확인
    if (abs((ord(data[i][0]) - ord(data[i + 1][0])) * (int(data[i][1]) - int(data[i + 1][1]))) == 2) and data[i] not in visited:
        visited.append(data[i])
    else:
        answer = "Invalid"

# 마지막 위치에서 첫 번째 위치로 갈 수 있는지 확인
if (abs((ord(data[-1][0]) - ord(data[0][0])) * (int(data[-1][1]) - int(data[0][1]))) == 2) and data[-1] not in visited:
    pass
else:
    answer = "Invalid"

print(answer)
