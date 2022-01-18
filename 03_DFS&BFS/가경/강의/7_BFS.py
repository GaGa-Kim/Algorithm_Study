# 7_BFS.py
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ') # 1 2 3 8 7 4 5 6
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 표현
graph = [
    [], # 인덱스 0은 사용하지 않도록 비워둠
    [2, 3, 8], # 1번 노드와 연결된 노드들
    [1, 7], # 2번 노드와 연결된 노드들
    [1, 4, 5], # 3번 노드와 연결된 노드들
    [3, 5], # 4번 노드와 연결된 노드들
    [3, 4], # 5번 노드와 연결된 노드들
    [7], # 6번 노드와 연결된 노드들
    [2, 6, 8], # 7번 노드와 연결된 노드들
    [1, 7] # 8번 노드와 연결된 노드들
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
# 처음에는 모두 방문하지 않은 것으로 표현
# [False, False, False, False, Flase, ... , False]
# 인덱스 0을 사용하지 않기 위해서 8 + 1 로 하나 더 크게 초기화
visited = [False] * 9

# 정의된 BFS 함수 호출 (시작 노드 : 1)
bfs(graph, 1, visited)