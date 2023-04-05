# n개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있을 때
# 수 x가 등장하는 횟수 계산 (단, 시간복잡도는 O(logN))
# 등장하지 않으면 -1 출력

# 원소들은 모두 정렬되어 있기 때문에 수열 내에 x가 존재한다면 
# 연속적으로 나열되어 있을 것
# => (x가 처음 등장하는 인덱스 - 마지막으로 등장하는 인덱스) 계산

# (1) 이진 탐색 함수 2개 작성-----------------------------------------------
# 정렬된 수열에서 값이 x인 원소의 개수 세는 함수
def count_by_value(array, x):
    n = len(array)
    
    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)
    
    # 수열에 x가 존재하지 않는 경우
    if a == None:
        return 0 # 0개
    
    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)
    
    # 개수 반환
    return b - a + 1
    

# target이 처음 등장하는 인덱스를 찾는 이진 탐색 함수
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

# target이 마지막으로 등장하는 인덱스를 찾는 이진 탐색 함수
def last(array, target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)
    
# 1 <= n <= 1,000,000 / -10^9 <= x <= 10^9
n, x = map(int, input().split())
# -10^9 <= 각 원소의 값 <= 10^9
array = list(map(int, input().split()))

# 값이 x인 데이터 개수 계산
count = count_by_value(array, x)

# 값이 x인 원소 존재하지 않으면
if count == 0:
    print(-1)
# 값이 x인 원소 존재하면
else:
    print(count)
    
    
# (2) bisect 라이브러리 이용-----------------------------------------------
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수 리턴
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

# 1 <= n <= 1,000,000 / -10^9 <= x <= 10^9
n, x = map(int, input().split())
# -10^9 <= 각 원소의 값 <= 10^9
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터 개수 계산
count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)