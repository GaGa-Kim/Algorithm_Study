# 456p 
# bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 효과적

# bisect_left(), bisect_right() ~> O(logN)
# 1) bisect_left(a, x)
# : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 찾는 메서드
# 2) bisect_right(a, x)
# : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 찾는 메서드
# 3) bisect(a, x)
# : bisect_right(a, x)와 같음


from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))     # 2
print(bisect_right(a, x))    # 4

# ----------------------------------------------------------------------------------
# bisect_left(), bisect_right()는 '정렬된 리스트'에서 
# '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때, 효과적으로 사용됨

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6
