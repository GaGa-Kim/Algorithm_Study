n, m = map(int, input().split())
picture = [[0] * 100 for _ in range(100)]

# 그림 가리기
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            picture[i - 1][j - 1] += 1

# 보이지 않는 그림의 개수
count = 0
for i in range(100):
    for j in range(100):
        if picture[i][j] > m:
            count += 1
print(count)