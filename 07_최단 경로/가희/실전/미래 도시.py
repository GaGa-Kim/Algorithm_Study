# 플로이드 워셜 (n 범위 100 이하)
# 1번 회사에서 x번 회사를 거쳐 k번 회사로 가는 최소 이동 시간 출력하는 프로그램
# k번 회사에 도달할 수 없으면 -1 출력

# 1번 ~ x번 ~ k번 최단 거리 = (1번 ~ x번 최단 거리) + (x번 ~ k번 최단 거리)

INF = int(1e9)

# 전체 회사 개수 n, 경로 개수 m (1 <= n,m <= 100)
n, m = map(int, input().split())
# 최단 거리 정보 저장할 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 간선 정보
for _ in range(m):
    # a와 b가 서로에게 가는 비용 1이라고 설정(양방향)
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    

# 1 <= k <= 100
x, k = map(int, input().split())

# 점화식 따라 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            
# 수행된 결과 출력
distance = graph[1][x] + graph[x][k]

if distance >= INF:
    print("-1")
else:
    print(distance)