import heapq
INF = int(1e9)

# 생명 테이블을 모두 무한으로 초기화
lifes = [[INF for _ in range(501)] for _ in range(501)]

# 위험한 구역
n = int(input())
danger = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    danger.append([x1, y1, x2, y2])

# 죽음의 구역
m = int(input())
death = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    death.append([x1, y1, x2, y2])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dijkstra():
    lifes[0][0] = 0
    q = []
    heapq.heappush(q, [0, 0, 0]) # 생명, x 좌표, y 좌표
    while q:
        life, x, y = heapq.heappop(q)
        if lifes[x][y] < life:
            continue
        # 4가지 이동 방향
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 좌표를 넘어갈 경우 가지 않음
            if nx < 0 or ny < 0 or nx > 500 or ny > 500:
                continue            
            # 죽음의 구역일 경우 가지 않음
            die = False
            for x1, y1, x2, y2 in death:
                if x1 <= nx <= x2 and y1 <= ny <= y2:
                    die = True
                    break
            if die:
                continue
            # 위험한 구역일 경우
            next_life = 0
            for x1, y1, x2, y2 in danger:
                if x1 <= nx <= x2 and y1 <= ny <= y2:
                    next_life += 1
                    break
            # 필요한 생명의 갯수가 더 적은 경우
            if lifes[nx][ny] > next_life + life:
                lifes[nx][ny] = next_life + life
                heapq.heappush(q, [next_life + life, nx, ny])
    return lifes[500][500]

answer = dijkstra()
if answer == INF:
    print(-1)
else:
    print(answer)