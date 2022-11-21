from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 인덱스와 종이 값을 튜플로 묶어서 덱에 저장
queue = deque(enumerate(map(int, input().split())))
answer = []
while queue:
    index, paper = queue.popleft()
    answer.append(index + 1)
    # 종이의 값이 양수일 경우
    if paper > 0:
        # 오른쪽으로 이동 (시계 방향)
        queue.rotate(-(paper - 1)) # pop을 하면서 왼쪽으로 1칸씩 이미 회전된 상태이므로 -1
    # 종이의 값이 음수일 경우
    elif paper < 0:
        # 왼쪽으로 이동 (반시계 방향)
        queue.rotate(-paper)
print(' '.join(map(str, answer)))
