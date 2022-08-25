import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
array = []
for _ in range(n):
    array.append(list(input().rstrip()))

# a와 b가 친구거나, a와 친구이고 b와 친구인 c
for c in range(n): 
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if array[a][b] == 'Y' or (array[a][c] == 'Y' and array[c][b] == 'Y'):
                graph[a][b] = 1

result = 0
for i in range(n):
    # 각 친구의 수를 셈
    count = 0
    for j in range(n):
        if graph[i][j] == 1:
            count += 1
    result = max(result, count)
print(result)