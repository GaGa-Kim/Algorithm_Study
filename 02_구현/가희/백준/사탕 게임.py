# 3085번
# 사탕이 채워진 상태가 주어졌을 때, 
# 상근이가 먹을 수 있는 사탕의 최대 개수 구하는 프로그램

# N*N 크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수 있다.
# 사탕의 색이 다른 인접한 두 칸을 고른다.
# 고른 칸에 들어있는 사탕으로 서로 교환한다.
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)을 고른 다음 
# 그 사탕을 모두 먹는다.

import sys
input = sys.stdin.readline

def check(color):
    n = len(color)
    maxCnt = 1

    for i in range(n):
        # 열 순회
        cnt = 1
        for j in range(1, n):
            if color[i][j] == color[i][j-1]:
            # 이전과 같으면 cnt + 1
                cnt += 1
            else:
            # 이전과 다르면 다시 1로 초기화
                cnt = 1
                
            if cnt > maxCnt:
                maxCnt = cnt

        # 행 순회
        cnt = 1
        for j in range(1, n):
            if color[j][i] == color[j-1][i]:
            # 이전과 같으면 cnt + 1
                cnt += 1
            else:
            # 이전과 다르면 다시 1로 초기화
                cnt = 1
                
            if cnt > maxCnt:
                maxCnt = cnt
    return maxCnt 

# 보드 크기 (3 <= N <= 50)
n = int(input())

# 사탕의 색상 (C: 빨, P: 파, Z: 초, Y: 노)
color = [list(input()) for _ in range(n)]
# 사탕 최대 개수
result = 0

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j+1 < n:
            color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
            
            tmp = check(color)
            
            if result < tmp:
                result = tmp
            
            # 바꿨던 것 원상복구
            color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
        
        #  행 바꾸기
        if i+1 < n:
            color[i][j], color[i+1][j] = color[i+1][j], color[i][j]
            
            tmp = check(color)
            
            if result < tmp:
                result = tmp;
                
            # 바꿨던 것 원상복구
            color[i][j], color[i+1][j] = color[i+1][j], color[i][j]

print(result)