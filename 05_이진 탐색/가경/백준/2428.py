import sys
input = sys.stdin.readline

n = int(input())
# i <= j 이어야 하므로 정렬
list = sorted(list(map(float, input().split())))

count = 0
for i in range(n - 1):
    start, end = i + 1, n - 1
    # i >= j * 0.9를 만족하는 요소의 최대 인덱스를 찾아냄
    while start <= end:
        mid = (start + end) // 2
        if list[i] >= list[mid] * (0.9):
            start = mid + 1
        else:
            end = mid - 1
    # 만족하는 요소 개수를 모두 더해줌
    count += end - i
print(count)