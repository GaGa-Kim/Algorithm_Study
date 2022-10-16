from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 모든 노드(과목)에 대한 수강 학기는 0으로 초기화
semesters = [0] * (n + 1)
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    # A번 과목이 B번 과목의 선수과목
    graph[a].append(b)
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 1))
            # 해당 과목의 수강 학기를 1로
            semesters[i] = 1
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now, semester = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                # 해당 과목의 수강 학기는 선수과목의 수강 학기 + 1
                q.append((i, semester + 1))
                semesters[i] = semester + 1

topology_sort()
print(*semesters[1:])
