# 다익스트라
# 도시 c에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간 출력하는 프로그램
# (단방향)

# 한 도시에서 다른 도시까지의 최단 거리 문제로 치환 가능,
# n과 m의 범위가 충분히 크므로 우선순위 큐 이용

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 도시 개수 n, 통로 개수 m, 메시지 보내고자 하는 도시 c
# (1 <= n <= 30,000 / 1 <= m <= 200,000 / 1 <= c <= n)
n, m, c = map(int, input().split())
# 각 노드 연결 정보
graph = [[] for _ in range(n+1)]
# 최단거리 테이블
distance = [INF] * (n+1)

# 통로(간선) 정보 (1 <= x,y <= n / 1 <= z <= 1,000)
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z
    graph[x].append((y, z))
    

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 현재 노드가 이미 처리된 적 있으면 무시
            continue
        # 현재 노드와 연결된 다른 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

# 도달할 수 있는 노드 개수(보낸 메시지를 받는 도시의 총 개수)
count = 0
# 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1
print(count - 1, max_distance)

