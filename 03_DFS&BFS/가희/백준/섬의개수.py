# 백준 4963번
# 각 테스트 케이스에 대해 섬의 개수를 세는 프로그램
# dfs 풀이 (음료수 얼려 먹기 문제랑 유사)

# 가로, 세로, 대각선 방향으로 연결
# 두 정사각형이 같은 섬에 있으려면 경로가 있어야 함
# 지도는 바다로 둘러싸여 있으며, 밖으로 나갈 수 x

import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
        # x는 세로, y는 가로 
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        
        if graph[x][y] == 1: # 땅이면
            graph[x][y] = 0 # 방문 처리
            # 8방향 반시계
            dfs(x-1, y)
            dfs(x-1, y-1)
            dfs(x, y-1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            dfs(x, y+1)
            dfs(x-1, y+1)
            return True
        return False
            

# 여러 개의 테스트 케이스
# 입력의 마지막 줄에는 0이 두 개 주어짐
while True:
    # 지도 너비 w, 높이 h (1 <= w,h <= 50)
    w, h = map(int, input().split())
    
    if not w and not h:
        break

    # 지도 (1: 땅, 0: 바다)
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt = 0
    for x in range(h):
        for y in range(w):
            #if graph[x][y] == 1:
            #    dfs(x,y)
            if dfs(x, y) == True: # dfs에 의해 방문처리 됐으면(=처음 방문이면)
                cnt += 1
    print(cnt)
