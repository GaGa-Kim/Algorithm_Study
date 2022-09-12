# 11403번
# 가중치 없는 방향 그래프 G가 주어졌을 때, 
# 모든 정점 (i,j)에 대해서 i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램
import sys
input = sys.stdin.readline

# 정점 개수 n (1 <= n <= 100)
n = int(input())

# 그래프 정보(인접 행렬)
graph = []
for _ in range(n):
    # 1 ~ 간선 o , 0 ~ 간선 x
    graph.append(list(map(int, input().split())))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])
    


