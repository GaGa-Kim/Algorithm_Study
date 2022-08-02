import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 지름길의 개수 N(간선의 개수)과 고속도로의 길이 D (노드의 개수)
n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
distance = [INF] * (d + 1)

# 모든 거리를 1로 초기화
for i in range(d):
    graph[i].append((i + 1, 1))

# 지름길이 있는 경우 업데이트
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d: # 지름길이 끝나는 지점이 목표 지점인 d보다 크다면 추가하지 않음 (목표 지점인 뒤로 돌아갈 수 없으므로)
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

dijkstra(0)
print(distance[d])
