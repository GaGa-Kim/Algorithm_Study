# 11286번
# 절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.
# 1. 배열에 정수 x(x != 0)를 넣는다.
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
#    절댓값이 가장 작은 값이 여러 개일 때는, 
#    최솟값을 출력하고 그 값을 배열에저 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import heapq
import sys
input = sys.stdin.readline

# 연산 개수 (1 ≤ n ≤ 100,000)
n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    
    # x != 0 이면 배열에 x 추가
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    # x == 0 이면 절댓값이 가장 작은 값 출력 뒤, 그 값 배열에서 제거
    else:
        if not len(heap):
            print(0)
        else:
            print(heapq.heappop(heap)[1])