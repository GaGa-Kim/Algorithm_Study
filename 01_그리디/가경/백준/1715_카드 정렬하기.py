import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(input()))

if n == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        # 가장 카드 묶음 크기가 작은 것끼리 먼저 더한 후 다시 넣어줌
        min1 = heapq.heappop(cards)
        min2 = heapq.heappop(cards)
        sum = min1 + min2
        answer += sum
        heapq.heappush(cards, sum)
    print(answer)
