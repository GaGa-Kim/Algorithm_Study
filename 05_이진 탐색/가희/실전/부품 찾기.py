# 매장에 부품이 n개 있을 때,
# 손님이 문의한 m개 종류의 부품이 매장에 모두 있는지 확인하는 프로그램
# 있으면 yes, 없으면 no 출력(공백 구분)

# 1) 이진 탐색 풀이-------------------------------------------
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
    
    
# 1 <= n <= 1,000,000
n = int(input())
array = list(map(int, input().split()))
array.sort()

# 1 <= m <= 100,000
m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        

# 2) 계수 정렬 풀이-------------------------------------------
n = int(input())
array = [0] * 1000001 # # 1 <= n <= 1,000,000 이므로

# 매장에 있는 전체 부품 번호 입력 받아 기록
for i in input().split():
    array[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        
    
# 3) 집합 자료형 이용 풀이--------------------------------------
# 집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때 유용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')