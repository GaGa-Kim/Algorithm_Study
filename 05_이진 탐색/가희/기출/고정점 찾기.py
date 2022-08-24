# 수열이 n개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있을 때
# 고정점이 있다면 고정점을 출력하는 프로그램
# 단, 시간복잡도는 O(logN), 고정점 없으면 -1 출력

# 고정점) 수열의 원소 중에서 그 값이 인덱스와 동일한 원소

def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid-1)
    else:
        return binary_search(array, mid+1, end)
    
# 1 <= n <= 1,000,000
n = int(input())
# n개의 원소 (-10^9 <= 각 원소의 값 <= 10^9)
array = list(map(int, input().split()))

index = binary_search(array, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)
