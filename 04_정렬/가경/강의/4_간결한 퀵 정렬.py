# 4_간결한 퀵 정렬.py
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    # 리스트 슬라이싱 이용
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    # 리스트 컴프리헨션 이용
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분 (tail 리스트에서 피벗보다 같거나 작은 것만 포함하는 리스트)
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분 (tail 리스트에서 피벗보다 같거나 큰 것만 포함하는 리스트)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]