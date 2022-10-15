import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for c in range(n): 
    for a in range(n):
        for b in range(n):
            if graph[a][b] > graph[a][c] + graph[c][b]:
                graph[a][b] = graph[a][c] + graph[c][b]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")