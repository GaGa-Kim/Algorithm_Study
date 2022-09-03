import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# a와 b가 친구거나, a와 친구이고 b와 친구인 c
for c in range(1, n + 1): 
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == 1 or graph[a][b] == 0:
                continue
            else:
                graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

# 회장 후보의 점수들
result = []
for i in range(1, n + 1):
    result.append(max(graph[i][1:]))

# 회장 후보의 점수와 그에 해당하는 회장 후보의 수
m = min(result)
print(m, result.count(m))
# enumerate() 함수를 통해 회장 후보 오름차순 출력 (인덱스 i, 원소 v)
for i, v in enumerate(result):
    if v == m: # 회장 후보의 점수와 동일하다면 후보
        print(i + 1, end=' ')