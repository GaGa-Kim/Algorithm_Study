# 1920번
# n개의 정수 A[1], A[2], ..., A[n]이 주어져 있을 때,
# 이 안에 x라는 정수가 존재하는지 알아내는 프로그램
# (존재하면 1, 존재하지 않으면 0 출력)

import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
        
    
# 1 <= n <= 100,000
n = int(input())

# n개의 정수
array = list(map(int, input().split()))
array.sort()

# 1 <= m <= 100,000
m = int(input())

# n개의 정수 안에 존재하는지 알아내야 할 정수 m개
# (-2^31 <= 정수 < 2^31)
int_list = list(map(int, input().split()))

for i in int_list:
    if binary_search(array, i, 0, n-1) != None:
        print(1)
    else: 
        print(0)