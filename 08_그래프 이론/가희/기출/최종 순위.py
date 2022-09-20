# 백준 3665번 / 위상 정렬
# 올해 대회에 1 ~ n번까지 팀이 참가
# 참가팀들의 작년 순위와 올해 작년에 비해 상대적인 순위가 바뀐 팀의 목록이 주어질 때,
# 올해 순위를 만드는 프로그램

# 1. 자기보다 낮은 등수를 가진 팀 가리키도록 방향 그래프 만듦
# 2. 상대적인 순위 바뀌는 경우, 해당 간선의 방향 반대로 변경
# 3. 이후 이 상태에서 위상 정렬 다시 수행
#   - 사이클이 발생하는 경우) 노드가 n번 나오기 전에 큐가 빌 경우
#   - 결과가 2개 이상) 특정 시점에 2개 이상의 노드가 큐에 한꺼번에 삽입되는 경우

from collections import deque

# 테스트 케이스 <= 100
for tc in range(int(input())):
    # 2 <= n <= 500
    n = int(input())
    # 진입차수
    indegree = [0] * (n+1)
    # 각 노드에 연결된 간선 정보(인접 행렬)
    graph = [[False] * (n+1) for i in range(n+1)]
    
    # 작년 순위 정보 ti (1 <= ti <= n) ~ 작년에 i등한 팀 번호
    data = list(map(int, input().split()))
    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i+1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1
    
    # 상대적인 등수가 바뀐 쌍의 수 (0 <= m <= 25000)
    m = int(input())
    # 변경된 순위 정보
    for i in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬    
    result = [] # 수행 결과
    q = deque()

    # 처음에는 진입차수가 0인 노드 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            
    certain = True  # 위상 정렬 결과가 오직 하나인지 여부
    cycle = False   # 그래프 내 사이클 존재 여부

    # 정확히 노드 개수만큼 반복
    for i in range(n):
        # 큐가 비어있다면 사이클 발생
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이면 정렬 결과 여러 개
        if len(q) >= 2:
            certain = False
            break
        
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 - 1
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                # 새롭게 진입차수가 0이 되는 노드 큐에 삽입
                if indegree[j] == 0:
                    q.append(j)
                
                
    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle:
        print("IMPOSSIBLE")
    # 위상 정렬 결과 여러 개인 경우
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()
