# 위상정렬
# n개의 강의 정보가 주어졌을 때, n개의 강의에 대하여 수강하기까지
# 걸리는 시간을 각각 출력하는 프로그램

# 각 강의 번호는 1부터 n까지로 구성, 각 줄은 -1로 끝남

from collections import deque
import copy
from re import L

# 1 <= n <= 500
n = int(input())
# 진입차수
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보 
graph = [[] for _ in range(n+1)]
# 각 강의 시간 (<= 100,000)
time = [0] * (n+1)

# 방향 그래프 간선 정보
for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과
    q = deque()
    
    # 처음에는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬 수행 결과 출력
    for i in range(1, n+1):
        print(result[i])
        
        
topology_sort()