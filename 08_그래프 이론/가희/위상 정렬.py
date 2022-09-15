# <위상 정렬> 
# 시간 복잡도) O(V + E) ~ 노드와 간선 확인하는 과정
# 1) 진입차수가 0인 노드를 큐에 넣는다.
# 2) 큐가 빌 때까지 다음 과정을 반복한다.
#   1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#   2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

from collections import deque

# 노드의 개수, 간선
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결리스트(그래프) 초기화
graph = [[] for _ in range(v+1)]

# 방향 그래프의 모든 간선 정보
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동 가능
    # 진입차수 1 증가
    indegree[b] += 1
    
    
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과
    q = deque()
    
    # 처음에는 진입차수가 0인 노드 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 - 1
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬 수행 결과 출력
    for i in result:    
        print(i, end=' ')
    
topology_sort()
