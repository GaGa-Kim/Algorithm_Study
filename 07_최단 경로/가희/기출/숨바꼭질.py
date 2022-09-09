# m개의 양방향 통로가 존재하는 1 ~ n번까지의 헛간에서 숨바꼭질
# 술래는 1번에서 출발하고, 1번으로부터 가장 먼 헛간에 숨을 것
# 숨을 헛간, 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간 개수 출력하는 프로그램

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 2 <= n <= 20,000 / 1 <= m <= 50,000
n, m = map(int, input().split())

# 시작 위치 - 1번 헛간
start = 1
# 노드 연결 정보
graph = [[] for i in range(n+1)]
# 최단 거리 테이블
distance = [INF] * (n+1)

# 간선 정보
for _ in range(m):
    # 1 <= a,b <= n
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
    

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 정보
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

# 최단 거리가 가장 먼 노드(숨을 헛간 번호)
max_node = 0
# 최단 거리가 가장 먼 노드의 거리
max_distance = 0
# 최단 거리가 가장 먼 노드와 최단 거리가 동일한 노드 리스트
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]            
    elif max_distance == distance[i]:
        result.append(i)
    
print(max_node, max_distance, len(result))
        
