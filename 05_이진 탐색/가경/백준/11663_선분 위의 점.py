import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))

# 선분 중 가장 작은 점 인덱스
def dot_min(a):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if dots[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

# 선분 중 가장 큰 점 인덱스
def dot_max(b):
    start, end = 0, n - 1
    while start <= end:
        mid = (start + end) // 2
        if b < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

for _ in range(m):
    a, b = map(int, input().split())
    print(dot_max(b) - dot_min(a) + 1)
