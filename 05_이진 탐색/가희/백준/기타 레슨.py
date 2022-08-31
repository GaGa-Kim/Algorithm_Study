# 2343번
# n개의 강의를 m개의 블루레이에 모두 같은 크기로 녹화하려고 할 때,
# 가능한 블루레이의 크기 중 최소를 구하는 프로그램
# 강의의 순서가 뒤바뀌면 안 됨

import sys
input = sys.stdin.readline

# 강의의 수 n (1 <= n <= 100,000), m (1 <= m <= n)
n, m = map(int, input().split())

# 강의의 길이(분 단위, 자연수, 길이 <= 10,000)
array = list(map(int, input().split()))

# start) 블루레이가 최소 9(가장 긴 길이)는 되어야 강의 담을 수 있음
# end) 블루레이가 45(길이 총 합)이상이면 블루레이 하나에 모든 강의 담을 수 있음
start, end = max(array), sum(array)

while start <= end:
    mid = (start + end) // 2 # 블루레이의 크기
    
    cnt = 0     # 레코드 개수
    tmp = 0     # 블루레이 하나 당 들어갈 강의 길이 합
    for i in range(n):
        if tmp + array[i] > mid:
            cnt += 1
            tmp = 0
        tmp += array[i]
    
    if tmp:
        cnt += 1
        
    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(start)
            
    