# 플로이드 워셜
# a번 학생의 성적이 b번 학생보다 낮으면 a->b로 표현 가능
# 학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 알 수 있는 학생 수 계산하는 프로그램

# a ~> b 또는 b ~> a로 도달 가능하면 성적 비교가능
# 모든 노드에 대해 다른 노드와 서로 도달 가능한지 체크
# 특정한 노드의 카운트 값이 n이면, 해당 노드의 정확한 순위 알 수 있음

import sys
input = sys.stdin.readline
INF = int(1e9)

# 학생 수 n (2 <= n <= 500), => 플로이드 워셜 가능  
# 두 학생의 성적을 비교한 횟수 m (2 <= m <= 10,000)
n, m = map(int, input().split())
# 최단 거리 정보 저장할 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 두 학생의 성적 비교 결과 나타내는 양의 정수 a, b (a < b)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
# 점화식 따라 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            

# 성적 순위를 정확히 알 수 있는 학생 수 
result = 0
# 각 학생들 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)