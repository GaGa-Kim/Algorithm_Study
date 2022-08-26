# 10816번
# 숫자 카드 n개를 가지고 있고, 정수 m개가 주어졌을 때
# 이 수가 적혀있는 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index
    
# 1 <= n <= 500,000
n = int(input())
# 숫자 카드에 적혀있는 정수 
# (-10,000,000 <= 정수 <= 10,000,000)
num_card = list(map(int, input().split()))
num_card.sort()

# 1 <= m <= 500,000
m = int(input())
# m개의 정수
array = list(map(int, input().split()))

for i in array: 
    print(count_by_range(num_card, i, i), end=' ')