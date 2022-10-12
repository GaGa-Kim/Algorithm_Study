n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def pooling(size, x, y):
    mid = size // 2
    # 행렬의 크기가 2 x 2일 때
    if size == 2:
        answer = [matrix[x][y], matrix[x + 1][y], matrix[x][y + 1], matrix[x + 1][y + 1]]
        answer.sort()
        return answer[-2]
    # 행렬의 크기가 2 x 2가 아닐 때, 2 x 2 행렬이 되도록 반복 
    left_top = pooling(mid, x, y)
    right_top = pooling(mid, x + mid, y)
    left_bottom = pooling(mid, x, y + mid)
    right_bottom = pooling(mid, x + mid, y + mid)
    answer = [left_top, right_top, left_bottom, right_bottom]
    answer.sort()
    return answer[-2]
print(pooling(n, 0, 0))