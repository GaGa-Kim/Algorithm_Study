from bisect import bisect_left, bisect_right
def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)
    return right_value - left_value

n = int(input())
array1 = list(map(int, input().split()))
array1.sort()
    
m = int(input())
array2 = list(map(int, input().split()))

for i in array2:
    print(count_by_range(array1, i, i), end=' ')
