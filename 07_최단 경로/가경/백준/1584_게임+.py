import heapq
INF = int(1e9)

# 그래프
graph = [[0 for _ in range(501)] for _ in range(501)]
# 생명 테이블을 모두 무한으로 초기화
lifes = [[INF for _ in range(501)] for _ in range(501)]

# 위험한 구역
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2) , max(y1, y2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if graph[i][j] == 0:
                graph[i][j] = 1

# 죽음의 구역
m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2) , max(y1, y2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            graph[i][j] = 2

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dijkstra():
    lifes[0][0] = 0
    q = []
    heapq.heappush(q, (0, 0, 0)) # 생명, x 좌표, y 좌표
    while q:
        life, x, y = heapq.heappop(q)
        if lifes[x][y] < life:
            continue
        # 4가지 이동 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx <= 500 and 0 <= ny <= 500:
                # 죽음의 구역일 경우 가지 않음
                if graph[nx][ny] == 2:
                    continue
                # 위험한 구역
                elif graph[nx][ny] == 1:
                    now_life = life + 1
                # 안전한 구역
                else:
                    now_life = life
                # 필요한 생명의 갯수가 더 적은 경우
                if now_life < lifes[nx][ny]:
                    lifes[nx][ny] = now_life
                    heapq.heappush(q, (now_life, nx, ny))

dijkstra()
answer = lifes[500][500]
if answer == INF:
    print(-1)
else:
    print(answer)