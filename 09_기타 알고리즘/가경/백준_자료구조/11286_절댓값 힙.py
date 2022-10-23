import sys, heapq
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    x = int(input())
    # x가 0이라면 배열에서 절댓값이 가장 작은 값을 출력
    if x == 0:
        if h:
            # 최소 힙
            print(heapq.heappop(h)[1])
        else:
            print(0)
    # x가 0이 아니라면 배열에 절댓값 x와 원래 x 값을 넣음
    # 힙을 튜플로 구성하면 맨 앞 절댓값 x만을 가지고 정렬
    else:
        heapq.heappush(h, (abs(x), x))