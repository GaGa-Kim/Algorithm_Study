import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for c in range(n): 
    for a in range(n):
        for b in range(n):
            if graph[a][b] == 1 or (graph[a][c] == 1 and graph[c][b] == 1):
                graph[a][b] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()