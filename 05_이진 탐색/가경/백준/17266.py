def binary_search(x, mid):
    # 모든 가로등 사이의 거리가 높이보다 클 경우
    if x[1] - x[0] > mid:
        return 0
    if x[-1] - x[-2] > mid:
        return 0
    for i in range(1, len(x) - 2):
        if (x[i + 1] - x[i]) / 2 > mid:
            return 0
    # 모든 가로등 사이의 거리가 높이보다 작거나 같을 경우
    return 1

n = int(input())
m = int(input())
# 가로등의 위치에 시작점과 마지막점을 따로 넣어줌
x = [0] + list(map(int, input().split())) + [n]

start, end = 0, n
answer = 0
while start <= end :
    # mid는 높이
    mid = (start + end) // 2
    if binary_search(x, mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1
print(answer)