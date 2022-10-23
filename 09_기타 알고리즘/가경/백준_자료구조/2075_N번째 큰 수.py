import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        # 힙의 크기를 n개로 유지
        if len(h) < n:
            heapq.heappush(h, number)
        else:
            # n번째 수와 비교해서 더 클 경우 담은 후, 가장 작은 값을 빼서 n개 유지
            if h[0] < number:
                heapq.heappush(h, number)
                heapq.heappop(h)
                
# 힙에는 n개가 존재하므로 그 중 가장 작은 값을 출력하면 n번째 큰 수
print(h[0])
