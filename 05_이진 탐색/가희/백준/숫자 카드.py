# 10815번
# 상근이가 숫자 카드 n개를 가지고 있고 정수 m개가 주어졌을 때, 
# 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지 구하는 프로그램
# (가지고 있으면 1, 아니면 0을 공백으로 구분해 출력)

import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
# 1 <= n <= 500,000
n = int(input())

# 숫자 카드에 적혀있는 정수 (-10,000,000 <= 정수 <= 10,000,000)
num_cards = list(map(int, input().split()))
num_cards.sort()

# 1 <= m <= 500,000
m = int(input())

# 상근이가 가지고 있는 숫자 카드인지 아닌지 구해야 할 정수
# (-10,000,000 <= 정수 <= 10,000,000)
array = list(map(int, input().split()))

for i in array:
    if binary_search(num_cards, i, 0, n-1) != None:
        print(1, end=' ')
    else:
        print(0, end=' ')
    