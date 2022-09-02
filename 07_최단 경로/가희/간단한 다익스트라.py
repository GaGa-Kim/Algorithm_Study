# O(V^2) ~ 전체 노드 개수가 5,000개 이하인 경우에 사용
# 처음에 각 노드에 대한 최단 거리를 담는 1차원 리스트를 선언한 뒤
# 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해
# 매 단계마다 1차원 리스트의 모든 원소 확인(순차탐색)

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n+1)]
# 방문 여부 
visited = [False] * (n + 1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미(방향그래프라고 가정)
    graph[a].appned((b, c))
    

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 리턴
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드의 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1] # j[0] ~ 노드, j[1] ~ 거리
    
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1): # 0 ~ n-2
        # 현재 최단 거리가 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우
    else:
        print(distance[i])
        