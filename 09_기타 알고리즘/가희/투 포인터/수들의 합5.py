# 백준 2018

n = int(input())

sum = 0

start, end = 0, 0
# 자기 자신 하나로 이루어진 경우의 수 미리 저장
count = 1 

while end < n:
    if sum < n:
        end += 1
        sum += end
    elif sum > n:
        sum -= start
        start += 1
    elif sum == n:
        end += 1
        sum += end
        count += 1

print(count)