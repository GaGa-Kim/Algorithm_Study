import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

# a와 b가 친구거나, a와 친구이고 b와 친구인 c
for c in range(n): 
    for a in range(n):
        for b in range(n):
            if a == b:
                graph[a][b] = 0
            else:
                # 직접 아는 사이인 것과 건너서 아는 사이 중에서 단계가 더 적은 것을 고름
                graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

bacon = []
for i in graph:
    # 케빈 베이컨의 수를 구함
    bacon.append(sum(i))
print(bacon.index(min(bacon)) + 1)