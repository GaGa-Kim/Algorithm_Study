# 맵 정보
graph = []
for _ in range(5):
    graph.append(list(map(str, input().split())))

# 4가지 이동 방향에 대한 리스트 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, s):
    if len(s) == 6:
        if s not in answer:
            answer.append(s)
        return True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            dfs(nx, ny, graph[nx][ny] + s)

answer = []
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(answer))