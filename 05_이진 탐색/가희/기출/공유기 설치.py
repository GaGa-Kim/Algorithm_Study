# 백준 2110번
# 각각 좌표를 가진 n개의 집이 수직선 위에 있을 때,
# 가장 인접한 두 공유기 사이의 거리를 최대로 하도록 c개의 공유기를 설치하는 프로그램

# => 이진 탐색으로 `가장 인접한 두 공유기 사이의 거리`를 조절해가며
#   매 순간 실제로 공유기를 설치하여 c보다 많은 개수로 설치할 수 있는지 체크

import sys
input = sys.stdin.readline

# 2 <= n <= 200,000 / 2 <= c <= n
n, c = list(map(int, input().split())) 

# 집의 좌표 xi (1 <= xi <= 1,000,000,000)
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()

# 집의 좌표 중 가장 작은 값 (최소 gap)
start = 1
# 집의 좌표 중 가장 큰 값 (최대 gap)
end = array[-1] - array[0]
result = 0

while (start <= end):
    mid = (start + end) // 2 # 가장 인접한 두 공유기 사이 거리
    value = array[0]
    count = 1
    
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    
    # c개 이상의 공유기 설치할 수 있는 경우 거리 증가
    if count >= c: 
        start = mid + 1
        result = mid # 최적의 결과 기록
    else: # c개 이상의 공유기를 설치할 수 없는 경우 거리 감소
        end = mid - 1
        
print(result)