import sys
input = sys.stdin.readline

n = int(input())

time = [[0] * 2 for _ in range(n)]
for i in range(n):
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end

# 끝나는 시간 오름차순으로 정렬한 후, 시작하는 시간의 오름차순으로 정렬
time.sort(key = lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]
for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)