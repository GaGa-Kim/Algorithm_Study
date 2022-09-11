# 1058번
# 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램

# 가장 유명한 사람 = 2-친구의 수가 가장 많은 사람
# a가 b의 2-친구가 되려면, 
# (1) 두 사람이 친구이거나,
# (2) a와 친구이고 b와 친구인 c가 존재해야 한다. => 플로이드 워셜
# a와 b가 친구면, b와 a도 친구, a와 a는 친구 아님
import sys
input = sys.stdin.readline

# 사람의 수 n (1 <= n <= 50)
n = int(input())
# 친구 정보
array = []
# 최단 거리 정보 저장할 2차원 리스트
graph = [[0] * n for _ in range(n)]

for _ in range(n):
    # 친구이면 Y, 아니면 N
    array.append(list(input()))

for c in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if array[a][b] == 'Y' or (array[a][c] == 'Y' and array[c][b] == 'Y'):
                graph[a][b] = 1

result = 0
for a in range(n):
    cnt = 0
    for b in range(n):
        if graph[a][b] == 1:
            cnt += 1
    result = max(result, cnt)

print(result)


