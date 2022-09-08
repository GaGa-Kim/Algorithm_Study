# 백준 11404번
# 플로이드 워셜
# 모든 도시 쌍 (A, B)에 대해서 A에서 B로 가는 데 필요한 비용의 최솟값을 구하는 프로그램
import sys
input = sys.stdin.readline
INF = int(1e9)

# 도시의 개수 n (1 <= n <= 100)
n = int(input())
# 버스의 개수 m (1 <= m <= 100,000)
m = int(input())
# 최단 거리 정보 저장할 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 버스 정보(처음에는 그 버스의 출발 도시, 비용 <= 100,000)
for _ in range(m):
    # a에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    # a와 b를 연결하는 간선 여러 개일 경우 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식 따라 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 0 출력
        if graph[a][b] == INF:
            print(0, end=" ")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=" ")
    print()
