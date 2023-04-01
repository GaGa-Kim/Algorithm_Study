# 11279번
# 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

import heapq
import sys
input = sys.stdin.readline

# 연산 개수 (1 ≤ n ≤ 100,000)
n = int(input())

heap = []
for _ in range(n):
    x = int(input())
    # x가 자연수면 배열에 x 추가
    if x :
        heapq.heappush(heap, -x)
    # x가 0이면 배열에서 최댓값 출력 뒤 그 값 배열에서 제거
    elif x == 0:
        # 배열이 비어있는데 최댓값 출력해야 하는 경우 0 출력
        if not len(heap):
            print(0)
        else:
            max_value = heapq.heappop(heap)
            print(-max_value)



"""
heapq는 최소힙만 지원하기 때문에 최대힙으로 이용하려면
heap에 넣어주는 수를 음수로 바꿔서 넣어준다.
"""