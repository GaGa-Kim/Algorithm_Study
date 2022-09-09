# n * n 크기의 2차원 공간이 있을 때, 
# [0][0] 위치에서 [n-1][n-1] 위치로 이동하는 최소 비용을 출력하는 프로그램
# 특정 위치에서 상하좌우 인접한 곳으로 1칸씩 이동 가능

# 입력이 2차원 배열로 들어오기 때문에 인접 행렬 이용 맵 정보 저장
# ~> n^2 = 125^2 > 10,000 이므로 플로이드 워셜 x, 다익스트라 o

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 시계방향(상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1 <= 테스트 케이스 수 <= 10
for t in range(int(input())):
    # 탐사 공간의 크기 n (2 <= n <= 125)
    n = int(input())
    
    # 전체 맵 정보 (0 <= 각 칸의 비용 <= 9)
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
        
    # 최단 거리 테이블
    distance = [[INF] * n for _ in range(n)]
    
    # 시작 위치 (0, 0)
    x, y = 0, 0
    q = [(graph[x][y], x, y)] # 시작 위치 큐에 삽입
    distance[x][y] = graph[x][y]
    
    # 다익스트라 수행
    while q:
        # 최단 거리가 가장 짧은 노드 정보
        dist, x, y = heapq.heappop(q)
        
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[x][y] < dist:
            continue
        
        # 현재 노드와 연결된 인접한 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][n-1])

