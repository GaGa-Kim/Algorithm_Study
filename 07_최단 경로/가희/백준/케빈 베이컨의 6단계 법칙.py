# 1389번
# 케빈 베이컨 수가 가장 작은 사람을 찾는 프로그램
# 케빈 베이컨 게임) 임의의 두 사람이 최소 몇단계 만에 이어질 수 있는지 계산하는 게임
# 케빈 베이컨) 게임 결과로 나오는 단계의 총합이 가장 적은 사람
import sys
input = sys.stdin.readline
INF = int(1e9)

# 유저 수 n (2 <= n <= 100), 친구 관계 수 m (1 <= m <= 5,000)
n, m = map(int, input().split())
# 최단 거리 정보
graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = graph[b-1][a-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
            else:
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = []
for i in graph:
    result.append(sum(i))

print(result.index(min(result)) + 1)