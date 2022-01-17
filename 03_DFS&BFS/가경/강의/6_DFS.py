# 6_DFS.py
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ') # 1 2 7 6 8 3 4 5
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [], 
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

# 정의된 DFS 함수 호출 (시작 노드 : 1)
dfs(graph, 1, visited)