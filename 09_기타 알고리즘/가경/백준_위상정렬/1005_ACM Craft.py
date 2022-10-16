from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    # 각 노드(건물)당 건설에 걸리는 시간
    time = [0] + list(map(int, input().split()))
    # 해당 건물까지 건설하기에 걸리는 최단 시간
    result = [0] * (n + 1)
    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (n + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for _ in range(n + 1)]

    # 방향 그래프의 모든 간선 정보를 입력 받기
    for _ in range(k):
        x, y = map(int, input().split())
        # x가 y의 건설 순서 선수
        graph[x].append(y)
        # 진입 차수를 1 증가
        indegree[y] += 1

    w = int(input())

    # 위상 정렬
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            # 건설 시간 갱신
            result[i] = time[i]
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 건설 시간 갱신
            result[i] = max(result[now] + time[i], result[i])
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    print(result[w])