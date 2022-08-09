# 18111번 (브루트포스)
# 땅 고르는 데 걸리는 최소 시간과 땅의 높이(최대 높이)

# <땅 고르기 작업>
# 1. 좌표 (i, j)의 가장 위에 있는 블록 제거 후 인벤에 넣기 (2초)
# 2. 인벤에서 블록 하나 꺼내서 좌표 (i, j) 맨 위에 쌓기 (1초)

import sys
input = sys.stdin.readline

# 가로, 세로, 인벤 블록 개수
n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

time, height = sys.maxsize, 0 # 시간, 층수

# 0 ~ 256층까지 반복
for h in range(257):
    max_h = min_h = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= h: # 블록이 층수보다 크면
                max_h += graph[i][j] - h
            else: # 블록이 층수보다 작으면
                min_h += h - graph[i][j]
    
    if max_h + b >= min_h:
        t = min_h + (max_h*2)
        if t <= time:
            time = t
            height = h
            
print(time, height)

#---------------------백준에서 데려옴..-------------------------
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
territory = []

for _ in range(n):
    territory += map(int, input().split())

big = max(territory)
small = min(territory)
_sum = sum(territory)

territory_dic = {}
for height in territory:
    territory_dic[height] = territory_dic.get(height, 0) + 1

time, height = 9999999999, 0
for temp in range(small, big+1):
    if _sum + b >= temp*n*m:
        temp_time = 0
        for key in territory_dic:
            if key < temp:
                temp_time += (temp-key)*territory_dic[key]
            elif key > temp:
                temp_time += (key-temp)*territory_dic[key]*2

        if temp_time <= time:
            time = temp_time
            height = temp

print(time, height)