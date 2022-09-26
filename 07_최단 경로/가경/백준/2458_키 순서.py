import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    tall, short = map(int, input().split())
    height[tall][short] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1): 
        for b in range(1, n + 1): 
            if height[a][b] == 1 or (height[a][k] == 1 and height[k][b] == 1):
                height[a][b] = 1

result = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 자기보다 크거나 작은 키를 비교하는 경우
        count += height[i][j] + height[j][i]
    # n - 1명과 모두 비교할 수 있다면
    if count == n - 1:
        result += 1
print(result)