# 1446번
# 지름길의 개수 n과 고속도로 길이 d가 주어질 때
# 세준이가 운전해야 하는 거리의 최솟값 구하는 프로그램
# 단방향 

# 시작노드 ~ 0, 도착노드 ~ d로 설정

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 1 <= n <= 12, 1 <= d <= 10,000
n, d = map(int, input().split()) 

start = 0
# 노드 연결 정보
graph = [[] for _ in range(d+1)]
# 최단 거리 테이블
distance = [INF] * (d+1)

# 일단 거리를 1로 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길이 있는 경우 업데이트
for _ in range(n):
    # 지름길 시작 위치, 도착 위치, 지름길 길이
    a, b, c = map(int, input().split())
    if b > d: # 도착 위치 > 고속도로 길이인 경우 추가 x
        continue
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[d])
