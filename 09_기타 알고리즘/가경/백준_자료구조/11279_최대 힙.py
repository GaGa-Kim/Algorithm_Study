import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    # x가 0이라면 배열에서 가장 큰 값 출력
    if x == 0:
        if h:
            # 최대 힙
            print(-heapq.heappop(h))
        else:
            print(0)
    # x가 자연수라면 배열에 x라는 값을 넣음
    else:
        heapq.heappush(h, -x)