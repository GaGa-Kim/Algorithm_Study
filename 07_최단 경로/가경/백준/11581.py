import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * n for _ in range(n)]

for i in range(n - 1):
    m = int(input())
    tmp = list(map(int, input().split()))
    for j in tmp:
        graph[i][j - 1] = 1

for c in range(n): 
        for a in range(n):
            for b in range(n):
                    graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

def func(graph):
    for a in range(n):
            for b in range(n):
                # 1번 노드에서 갈 수 있는 사이클의 경우만
                if 0 < graph[0][b] < INF:
                    if  (0 < graph[a][b] < INF) and (0 < graph[b][a] < INF):
                        return 1
    return 0

# 자기 자신으로 향하는 값이 INF가 아닌 다른값이 들어있다면 나 자신으로 돌아왔다는 뜻
if func(graph):
    print("CYCLE")
else:
    print("NO CYCLE")