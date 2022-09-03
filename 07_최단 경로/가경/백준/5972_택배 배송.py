import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
# 헛간 지도
graph = [[] for _ in range(n + 1)]
# 최단으로 지나간 소들 테이블 
distance = [INF] * (n + 1) 

# 모든 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q: 
        dist, now = heapq.heappop(q) # 거리, 노드
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1] 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
print(distance[n])