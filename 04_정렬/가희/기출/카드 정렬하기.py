# 백준 1715번
# n개의 숫자 카드 묶음의 각각 크기가 주어질 때, 
# 최소한 몇 번의 비교가 필요한지 구하는 프로그램

# 각 묶음의 카드의 수를 A, B라 할 때 두 묶음을 하나로 만드는 데에는
# A + B번의 비교해야 함

import heapq
import sys
input = sys.stdin.readline

# 1 <= n <= 100,000
n = int(input())

# 우선순위 큐(힙)에 원소 넣었다 빼는 것만으로도 정렬 가능
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0

# 힙에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    
    # 카드 묶음 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)
    
print(result)


