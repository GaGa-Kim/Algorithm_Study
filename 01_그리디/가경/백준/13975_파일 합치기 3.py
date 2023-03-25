import sys, heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)

    if k == 1:
        print(files[0])
        break

    answer = 0
    while len(files) > 1:
        # 가장 파일 크기가 작은 장끼리 먼저 더한 후 다시 넣어줌
        min1 = heapq.heappop(files)
        min2 = heapq.heappop(files)
        sum = min1 + min2
        answer += sum
        heapq.heappush(files, sum)
    print(answer)