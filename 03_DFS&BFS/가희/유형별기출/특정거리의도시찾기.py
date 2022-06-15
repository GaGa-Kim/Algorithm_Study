# 백준 18352번
# X로부터 출발하여 도달할 수 있는 도시 중에서,
# 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램

# X ~> X 최단 거리는 항상 0
from collections import deque

# 도시 개수 N, 도로 개수 M, 거리 정보 K, 시작점 X
# ( 2<=N<=300,000, 1<=M<=1,000,000, 1<=K<= 300,000, 1<=X<=N )
n, m, k, x = map(int, input().split())

# 도로 정보 ( A B, 1<=A, B<=N, A와 B는 서로 다른 자연수 )
# A번 도시에서 B번 도시로 이동하는 단방향 도로 존재한다는 의미
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
# 출발 도시 X에서 X로 가는 최단 거리는 항상 0이라고 가정
distance[x] = 0 

# 모든 간선의 비용이 동일할 때는(1) 너비 우선 탐색 이용 ~> 최단 거리 찾음
# => 모든 도시까지의 최단 거리 계산한 뒤, 각 최단 거리를 하나씩 확인하며 그 값이 K이면 출력
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시이면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
    
# 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if check == False:
    print(-1)