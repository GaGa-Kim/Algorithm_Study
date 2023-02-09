# 백준 4963번
# 각 테스트 케이스에 대해 섬의 개수를 세는 프로그램
# bfs 풀이 (음료수 얼려 먹기 문제랑 유사)

# 가로, 세로, 대각선 방향으로 연결
# 두 정사각형이 같은 섬에 있으려면 경로가 있어야 함
# 지도는 바다로 둘러싸여 있으며, 밖으로 나갈 수 x

from collections import deque
import sys
sys.setrecursionlimit(10000)

def bfs(x, y):
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    
    q = deque()
    q.append([x, y])
    graph[x][y] = 0 # 방문 처리
    
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])
                
while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
        
    cnt = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)